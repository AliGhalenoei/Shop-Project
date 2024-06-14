from django.test import TestCase

from content.models import *


class TestCategoryModel(TestCase):

    def setUp(self) -> None:
        self.category = Category.objects.create(
            title = 'Test title',
            slug = 'test-slug'
        )

    def test_method_str(self):
        self.assertEqual(str(self.category),'Test title')


class TestProductModel(TestCase):

    def setUp(self) -> None:
        self.product = Product.objects.create(
            title = 'Test title',
            body = 'Test body',
            price = 1000,
            slug = 'test-slug'
        )
    
    def test_method_str(self):
        self.assertEqual(str(self.product),'Test title')

