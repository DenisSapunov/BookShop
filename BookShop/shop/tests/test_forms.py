from django.test import TestCase
from shop.forms import RateForm


class RateFormTest(TestCase):

    def test_rate_right(self):
        form_data = {'rate': 5}
        form = RateForm(form_data)
        self.assertTrue(form.is_valid())

    def test_rate_wrong(self):
        form_data = {'rate': 6}
        form = RateForm(form_data)
        self.assertFalse(form.is_valid())

