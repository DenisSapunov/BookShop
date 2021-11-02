from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from cart.cart import Cart
from shop.models import Book


class TestCartView(TestCase):
    def setUp(self):
        image = SimpleUploadedFile(name='test.jpg', content=b'\x00')
        self.book = Book.objects.create(name='Book',
                                        slug='book',
                                        description='test',
                                        pub_year=12,
                                        price=7.40,
                                        language='test',
                                        num_pages=33,
                                        availability=True,
                                        image=image)
        self.client = Client()

    def test_cart_add_POST(self):
        response = self.client.post('/cart/add/1/')
        self.assertEqual(response.status_code, 302)

    def test_cart_detail_GET(self):
        response = self.client.get(reverse('cart:cart_detail'))
        self.assertEqual(response.status_code, 200)