from django.test import SimpleTestCase
from django.urls import reverse , resolve

from content import views


class TestUrls(SimpleTestCase):

    def test_categorys(self):
        url = reverse('categorys')
        self.assertEqual(resolve(url).func.view_class,views.CategorysAPIView)

    def test_products(self):
        url = reverse('products')
        self.assertEqual(resolve(url).func.view_class,views.ProductsAPIView)

    def test_product(self):
        url = reverse('product' , args=['slug-pro'])
        self.assertEqual(resolve(url).func.view_class,views.RetrieveProductAPIView)


