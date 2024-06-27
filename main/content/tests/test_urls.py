from django.test import SimpleTestCase
from django.urls import reverse , resolve

from content import views


class TestUrls(SimpleTestCase):

    def test_categorys_url(self):
        url = reverse('categorys')
        self.assertEqual(resolve(url).func.view_class,views.CategorysAPIView)

    def test_products_url(self):
        url = reverse('products')
        self.assertEqual(resolve(url).func.view_class,views.ProductsAPIView)

    def test_product_url(self):
        url = reverse('product' , args=['slug-pro'])
        self.assertEqual(resolve(url).func.view_class,views.RetrieveProductAPIView)

    def test_filter_products_url(self):
        url = reverse('filter_products' , args=['slug-pro'])
        self.assertEqual(resolve(url).func.view_class,views.FilterProductAPIView)

    def test_related_products_url(self):
        url = reverse('related_products',args=['slug_product'])
        self.assertEqual(resolve(url).func.view_class,views.RelatedProductAPIView)


