from django.test import TestCase

from accounts.models import User
from accounts.forms import UserCreationForm


class TestUserCreationForm(TestCase):

    @classmethod
    def setUpTestData(cls) -> None:
        User.objects.create_user(
            phone = '09999999999',
            username = 'Ali',
            password = 'Ali1234'
        )

    def test_valid_data(self):
        form = UserCreationForm(data={
            'phone' : '09222222222',
            'username' : 'mmd',
            'password':'mmd123',
            'password2':'mmd123'
        })

        self.assertTrue(form.is_valid())


    def test_empty_data(self):
        form = UserCreationForm(data={})

        self.assertFalse(form.is_valid())
