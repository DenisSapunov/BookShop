from django.test import TestCase
from orders.forms import OrderCreateForm


class OrderFormTest(TestCase):

    def test_order_right(self):
        form_data = {'first_name': 'test_first_name', 'last_name': 'test_last_name',
                     'email': 'test@email.com', 'address': 'test_address',
                     'postal_code': 'postal', 'city': 'test_city'}
        form = OrderCreateForm(form_data)
        self.assertTrue(form.is_valid())

    def test_order_wrong(self):
        form_data = {'first_name': 'test_first_name', 'last_name': 'test_last_name',
                     'email': 'test@email.com', 'address': 'test_address',
                     'postal_code': 'test_postal_code', 'city': 'test_city'}
        form = OrderCreateForm(form_data)
        self.assertFalse(form.is_valid())
