from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse


class TestAccountsView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_register_page_GET(self):
        response = self.client.get(reverse('accounts:register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/register.html')

    def test_register_page_POST(self):
        response = self.client.post('/accounts/register', data={'username': 'test_username',
                                                                'password1': 'test_password',
                                                                'email': 'test@test.com',
                                                                })
        self.assertEqual(response.status_code, 200)

    def test_logout(self):
        response = self.client.get(reverse('accounts:logout'))
        self.assertEqual(response.status_code, 302)

    def test_login_GET(self):
        response = self.client.get(reverse('accounts:login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/login.html",)

    def test_login_POST(self):
        response = self.client.post('/accounts/login')
        self.assertEqual(response.status_code, 200)

    def test_user_page_GET(self):
        self.client.force_login(user=User.objects.create(username='test_user_name', password='3333333'), backend=None)
        response = self.client.get(reverse('accounts:user_page'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/user.html", )