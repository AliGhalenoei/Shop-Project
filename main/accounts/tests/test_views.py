from django.test import TestCase , Client
from django.urls import reverse

from rest_framework.test import APIClient

from accounts.models import OTP
from accounts.forms import *
from accounts.serializers import *



# Problem...
class TestVeryfyOtpAPIView(TestCase):

    def test_veryfy_otp_APIView_POST(self):
        pass

# Problem...
class TestUserRegisterAPIView(TestCase):

    def test_user_register_APIView_POST(self):
        pass