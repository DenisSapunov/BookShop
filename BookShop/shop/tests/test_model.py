from decimal import Decimal
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from shop.models import Book, Category, Author


class BookModelTest(TestCase):
    # c = category = Category.objects.create(name='test_', slug='test_')
    # a = author = Author.objects.create(name='test_')

    def setUp(self):
        image = SimpleUploadedFile(name='test.jpg', content=b'\x00')
        Book.objects.create(name='Book',
                            slug='book',
                            description='test',
                            pub_year=12,
                            price=7.40,
                            language='test',
                            num_pages=33,
                            availability=True,
                            image=image)

        Category.objects.create(name='test', slug='test')
        self.category = Category.objects.first()

        Author.objects.create(name='test')
        self.author = Author.objects.first()

    def test_name(self):
        book = Book.objects.first()
        self.assertEqual(book.name, 'Book')

    def test_name_max_length(self):
        book = Book.objects.first()
        max_length = book._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_description(self):
        book = Book.objects.first()
        self.assertEqual(book.description, 'test')

    def test_price(self):
        book = Book.objects.first()
        self.assertEqual(book.price, Decimal('7.40'))

    def test_num_pages(self):
        book = Book.objects.first()
        self.assertEqual(book.num_pages, 33)

    def test_pub_year(self):
        book = Book.objects.first()
        self.assertEqual(book.pub_year, 12)

    def test_language(self):
        book = Book.objects.first()
        self.assertEqual(book.language, 'test')

    def test_language_max_length(self):
        book = Book.objects.first()
        max_length = book._meta.get_field('language').max_length
        self.assertEqual(max_length, 255)

    def test_availability(self):
        book = Book.objects.first()
        self.assertEqual(book.availability, True)

    def test_slug(self):
        book = Book.objects.first()
        self.assertEqual(book.slug, 'book')

    def test_slug_max_length(self):
        book = Book.objects.first()
        max_length = book._meta.get_field('slug').max_length
        self.assertEqual(max_length, 300)

    def test_category_name(self):
        self.assertEqual(self.category.name, 'test')

    def test_category_name_max_length(self):
        max_length = self.category._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    def test_category_slug(self):
        self.assertEqual(self.category.name, 'test')

    def test_category_slug_max_length(self):
        max_length = self.category._meta.get_field('slug').max_length
        self.assertEqual(max_length, 300)

    def test_author_name(self):
        self.assertEqual(self.author.name, 'test')

    def test_author_name_max_length(self):
        max_length = self.author._meta.get_field('name').max_length
        self.assertEqual(max_length, 250)
