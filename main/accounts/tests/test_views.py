from django.test import TestCase , Client
from django.urls import reverse

from rest_framework.test import APIClient

from accounts.models import OTP
from accounts.forms import *
from accounts.serializers import *


class TestUserAuthenticationView(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_user_authentication_APIView_valid_POST(self):
        response = self.client.post(reverse('authentication'),data={
            'phone':'09101111111'
        })
        self.assertEqual(response.status_code,302)

    def test_user_authentication_APIView_invalid_POST(self):
        response = self.client.post(reverse('authentication'),data={})
        self.assertEqual(response.status_code,400)

# Problem...
class TestVeryfyOtpAPIView(TestCase):

    def test_veryfy_otp_APIView_POST(self):
        pass

# Problem...
class TestUserRegisterAPIView(TestCase):

    def test_user_register_APIView_POST(self):
        pass