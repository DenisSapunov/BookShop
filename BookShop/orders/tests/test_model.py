from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from orders.models import OrderItem, Order
from decimal import Decimal
from shop.models import Book


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

        order = Order.objects.create(
            first_name='test_first_name',
            last_name='test_last_name',
            email='test@test.com',
            address='test_address',
            postal_code='postal',
            city='test_city',
            paid=False)

        order_item = OrderItem.objects.create(
            price=Decimal('12.50'),
            quantity=1,
            book=Book.objects.first(),
            order=Order.objects.first())

        self.order = Order.objects.first()
        self.order_item = OrderItem.objects.first()

    def test_order_first_name(self):
        self.assertEqual(self.order.first_name, 'test_first_name')

    def test_order_first_name_max_length(self):
        max_length = self.order._meta.get_field('first_name').max_length
        self.assertEqual(max_length, 50)

    def test_order_last_name(self):
        self.assertEqual(self.order.last_name, 'test_last_name')

    def test_order_last_name_max_length(self):
        max_length = self.order._meta.get_field('last_name').max_length
        self.assertEqual(max_length, 50)

    def test_order_email(self):
        self.assertEqual(self.order.email, 'test@test.com')

    def test_order_address(self):
        self.assertEqual(self.order.address, 'test_address')

    def test_order_address_max_length(self):
        max_length = self.order._meta.get_field('address').max_length
        self.assertEqual(max_length, 250)

    def test_order_postal_code(self):
        self.assertEqual(self.order.postal_code, 'postal')

    def test_order_postal_code_max_length(self):
        max_length = self.order._meta.get_field('postal_code').max_length
        self.assertEqual(max_length, 8)

    def test_order_city(self):
        self.assertEqual(self.order.city, 'test_city')

    def test_order_city_max_length(self):
        max_length = self.order._meta.get_field('city').max_length
        self.assertEqual(max_length, 50)

    def test_order_paid(self):
        self.assertFalse(self.order.paid)

    def test_order_item_price(self):
        self.assertEqual(self.order_item.price, Decimal('12.50'))

    def test_order_item_quantity(self):
        self.assertEqual(self.order_item.quantity, 1)

