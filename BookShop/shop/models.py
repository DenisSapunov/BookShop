import os
from django.core.files import File
from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from urllib.request import urlretrieve
from django.core.validators import MaxValueValidator, MinValueValidator


class Book(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='название')
    slug = models.SlugField(max_length=300, unique=True, verbose_name="SLUG")
    description = models.TextField(verbose_name='описание')
    pub_year = models.IntegerField(verbose_name='Год публикации', null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    language = models.CharField(max_length=255, verbose_name='Язык', default="Русский")
    num_pages = models.IntegerField(verbose_name='Количество страниц', null=True)
    author = models.ManyToManyField('Author', related_name='books', null=True)
    category = models.ManyToManyField('Category', related_name='books', null=True)
    image = models.ImageField(upload_to='media/books/', verbose_name='Изображение', null=True)
    image_url = models.URLField(null=True)
    availability = models.BooleanField(default=True, verbose_name='Наличие')

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"

    def __str__(self):
        return self.name

    def get_remote_img(self):
        if self.image_url and not self.image:
            result = urlretrieve(self.image_url)
            self.image.save(
                os.path.basename(self.image_url),
                File(open(result[0], 'rb'))
            )
            self.save()

    def get_category(self):
        return "\n".join([p.name for p in self.category.all()])

    get_category.__name__ = "категория"

    def get_author(self):
        return "\n".join([p.name for p in self.author.all()])

    get_author.__name__ = 'автор'


class Author(models.Model):
    name = models.CharField(max_length=250, null=True)

    class Meta:
        verbose_name = 'Автор'
        verbose_name_plural = "Авторы"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='назавание')
    slug = models.SlugField(max_length=300, unique=True, verbose_name="SLUG")

    class Meta:
        ordering = ('-name',)
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'category_id': self.pk})


class UserBookRate(models.Model):
    RATE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )

    user = models.ForeignKey(User, related_name='user_rate', on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_rate')
    rate = models.IntegerField(choices=RATE_CHOICES, blank=True,
                               validators=[MaxValueValidator(5), MinValueValidator(1)])

    class Meta:
        verbose_name = 'Рейтинг'
        verbose_name_plural = "Оценки пользователей"

    def __str__(self):
        return f"{self.user.username}"
