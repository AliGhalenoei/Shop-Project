from django.test import SimpleTestCase
from django.urls import reverse , resolve

from accounts import views

class TestUrls(SimpleTestCase):

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class,views.UserLoginAPIView)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func.view_class,views.UserLogoutAPIView)

    def test_authentication_url(self):
        url = reverse('authentication')
        self.assertEqual(resolve(url).func.view_class,views.UserAuthenticationAPIView)

    def test_veryfy_url(self):
        url = reverse('veryfy')
        self.assertEqual(resolve(url).func.view_class,views.VeryfyOtpAPIView)

    def test_register_url(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func.view_class,views.UserRegisterAPIView)