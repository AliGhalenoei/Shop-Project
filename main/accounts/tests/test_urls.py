from django.test import SimpleTestCase
from django.urls import reverse , resolve

from accounts import views

class TestUrls(SimpleTestCase):

    def test_login_url(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func.view_class,views.UserLoginAPIView)