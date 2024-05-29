from django.test import TestCase

from accounts.models import User , OTP


class TestUserModel(TestCase):

    def setUp(self) -> None:
        self.user_instance = User.objects.create_user(
            phone = '09999999999',
            username = 'jack',
            password = 'TEST'
        )

    def test_method_str(self):
        self.assertEqual(str(self.user_instance),'jack')


class TestOtpModel(TestCase):

    def setUp(self) -> None:
        self.otp_instance = OTP.objects.create(
            phone = '09666666666',
            code = 1234
        )

    def test_method_str(self):
        self.assertEqual(str(self.otp_instance),'09666666666 Code Veryfy : 1234')