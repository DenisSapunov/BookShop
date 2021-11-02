from django.test import TestCase
from cart.forms import CartAddBookForm

class TestCartAdd(TestCase):

    def test_quantity_right(self):
        form_data = {'quantity': 5}
        form = CartAddBookForm(form_data)
        self.assertTrue(form.is_valid())

    def test_quantity_wrong(self):
        form_data = {'rate': 19}
        form = CartAddBookForm(form_data)
        self.assertFalse(form.is_valid())
