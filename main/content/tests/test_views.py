from django.test import TestCase , Client
from django.urls import reverse

from rest_framework.test import APIClient

from content.models import Product , Category



class TestCategorysAPIView(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_request_GET(self):
        response = self.client.get(reverse('categorys'))
        self.assertEqual(response.status_code,200)


class TestProductsAPIView(TestCase):

    def setUp(self) -> None:
        self.client = Client()

    def test_request_GET(self):
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code,200)


class TestRetrieveProductAPIView(TestCase):

    def setUp(self) -> None:
        self.client = Client()

        Product.objects.create(
            title = 'Test title',
            body = 'Test body',
            price = 1000,
            slug = 'test-slug'
        )

    def test_request_GET(self):
        response = self.client.get(reverse('product',args=['test-slug']))
        self.assertEqual(response.status_code,200)

        
class TestFilterProductAPIView(TestCase):

    def setUp(self) -> None:
        self.client = Client()

        Category.objects.create(
            title = 'Test title',
            slug = 'slug-tes',
            id = 6
        )

        Product.objects.create(
            title = 'Test title',
            body = 'Test body',
            price = 1000,
            slug = 'test-slug'
        )

    def test_request_GET(self):
        response = self.client.get(reverse('filter_products',args=['slug-tes']))
        self.assertEqual(response.status_code,200)


class TestRelatedProductAPIView(TestCase):

    def setUp(self) -> None:

        self.client = Client()
        Product.objects.create(
            title = 'Test title',
            body = 'Test body',
            price = 1000,
            slug = 'test-slug1'
        )
        return super().setUp()
    
    def test_method_GET(self):
        response = self.client.get(reverse('related_products',args=['test-slug1']))
        self.assertEqual(response.status_code,200)