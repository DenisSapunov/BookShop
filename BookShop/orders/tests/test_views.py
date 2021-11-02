from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from orders.models import Order, OrderItem, Book
from decimal import Decimal


class TestOrderView(TestCase):

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
        self.client = Client()

    def test_order_create_GET_without_login(self):
        response = self.client.get(reverse('order:order_create'))
        self.assertEqual(response.status_code, 302)

    def test_order_create_GET_with_login(self):
        self.client.force_login(user=User.objects.create(username='test_user_name', password='3333333'), backend=None)
        response = self.client.get(reverse('order:order_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order_create.html')

    def test_order_create_POST(self):
        self.client.force_login(user=User.objects.create(username='test_user_name', password='3333333'), backend=None)
        response = self.client.post('/orders/create/',
                                    data={'first_name': 'test_first_name', 'last_name': 'test_last_name',
                                          'email': 'test@email.com', 'address': 'test_address',
                                          'postal_code': 'postal', 'city': 'test_city'})
        self.assertEquals(response.status_code, 302)

    def test_order_in_process_GET(self):
        self.client.force_login(user=User.objects.create(username='test_user_name', password='3333333'), backend=None)
        response = self.client.get(reverse('order:in_process_order'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/in_process_order.html')

    def order_history_GET(self):
        self.client.force_login(user=User.objects.create(username='test_user_name', password='3333333'), backend=None)
        response = self.client.get(reverse('order:order_history'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'orders/order_history.html')
