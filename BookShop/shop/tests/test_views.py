from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase, Client
from django.urls import reverse
from shop.models import Book, Category


class TestShopView(TestCase):

    def setUp(self):
        self.category = Category.objects.create(name='test', slug='test')
        self.detail_url = reverse('shop:book_detail', args=['book'])
        self.test_user = User.objects.create(username='test', password='12345678')
        self.client = Client()
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

    def test_catalog_GET(self):
        response = self.client.get(reverse('shop:main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/catalog.html')

    def test_book_detail_GET(self):
        response = self.client.get(reverse('shop:book_detail', args=['book']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/book_detail.html')

    def test_book_detail_rate_post(self):
        self.client.force_login(user=User.objects.create(username='testt_user_name', password='3333333'), backend=None)
        response = self.client.post('/books/book', data={'rate': 3})
        self.assertEquals(response.status_code, 302)

    def test_searchbar_GET(self):
        response = self.client.get(reverse('shop:search'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/searchbar.html')

    def test_category_detail_GET(self):
        response = self.client.get(reverse('shop:category_detail', args=['test']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop/category_detail.html')
