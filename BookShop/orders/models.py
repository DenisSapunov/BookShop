from django.db import models
from django.urls import reverse

from shop.models import Book
from django.contrib.auth.models import User


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order_user', null=True)
    first_name = models.CharField(max_length=50, null=True, blank=False, verbose_name="Имя")
    last_name = models.CharField(max_length=50, null=True, blank=False, verbose_name="Фамилия")
    email = models.EmailField(null=True, blank=False, verbose_name="email")
    address = models.CharField(max_length=250, null=True, blank=False, verbose_name="адресс")
    postal_code = models.CharField(max_length=8, null=True, blank=False, verbose_name="почтовый индекс")
    city = models.CharField(max_length=50, null=True, blank=False, verbose_name="город")
    created = models.DateTimeField(auto_now_add=True, verbose_name="выполнен")
    updated = models.DateTimeField(auto_now=True, verbose_name="обновлён")
    paid = models.BooleanField(default=False, null=True, blank=False, verbose_name="оплачен")
    completed = models.BooleanField(default=False, verbose_name="закончен", null=True)

    class Meta:
        ordering = ('-created',)
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_total_cost(self):
        return sum(item.get_cost for item in self.items.all())

    def get_absolute_url(self):
        return reverse('orders:in_process_order', kwargs={'order_id': self.pk})


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    book = models.ForeignKey(Book, related_name='order_item', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return 'Order {}'.format(self.id)

    def get_cost(self):
        return self.price * self.quantity

    def get_absolute_url(self):
        return reverse('orders:in_process_order', kwargs={'order_id': self.pk})
