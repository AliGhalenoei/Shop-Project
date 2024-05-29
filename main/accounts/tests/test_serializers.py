from django.test import TestCase

from accounts.models import User
from accounts.serializers import (
    UserAuthenticationSerializer,
    UserRegisterSerializer
)



class TestUserAuthenticationSerializer(TestCase):

    serializer_class = UserAuthenticationSerializer

    def setUp(self) -> None:
        User.objects.create_user(
            phone = '09999999999',
            username = 'Test',
            password = 'Test1234'
        )

    def test_valid_data(self):
        serializer = self.serializer_class(data = {
            'phone':'09234325671'
        })
        self.assertTrue(serializer.is_valid())

    def test_empty_valid_data(self):
        serializer = self.serializer_class(data = {})
        self.assertFalse(serializer.is_valid())

    def test_exist_phone(self):
        serializer = self.serializer_class(data = {
            'phone':'09999999999'
        })
        self.assertFalse(serializer.is_valid())  
        self.assertEqual(len(serializer.errors), 1) 



class TestUserRegisterSerializer(TestCase):

    serializer_class = UserRegisterSerializer

    def setUp(self) -> None:
        User.objects.create_user(
            phone = '09999999999',
            username = 'Test',
            password = 'Test1234'
        )

    def test_valid_data(self):
        serializer = self.serializer_class(data = {
            'username':'Ali',
            'password':'Ali1234',
            'password2':'Ali1234'
        })
        self.assertTrue(serializer.is_valid())

    def test_empty_valid_data(self):
        serializer = self.serializer_class(data = {})
        self.assertFalse(serializer.is_valid())

    def test_exist_username(self):
        serializer = self.serializer_class(data = {
            'username':'Test',
            'password':'1234',
            'password2':'1234'
        })
        self.assertFalse(serializer.is_valid())
        self.assertEqual(len(serializer.errors),1)

    def test_match_password(self):
        test_data = {
            'username':'Test',
            'password':'1234',
            'password2':'1234'
        }

        serializer = self.serializer_class()
        validate_data = serializer.validate(test_data)

        self.assertEqual(validate_data,test_data)





    
