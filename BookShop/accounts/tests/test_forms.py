from django.test import TestCase
from accounts.forms import NewUserForm


class RateFormTest(TestCase):

    def test_user_form_right(self):
        form_data = {'username': 'testuser', 'email': 'test@test.com', 'password1': 'Test_test3',
                     'password2': 'Test_test3'}
        form = NewUserForm(form_data)
        self.assertTrue(form.is_valid())

    def test_user_form_wrong(self):
        form_data = {'username': 'testuser', 'email': 'test@test.com', 'password1': 'test_test',
                     'password2': 'test_test_test'}
        form = NewUserForm(form_data)
        self.assertFalse(form.is_valid())
