from django.test import TestCase
from model_bakery import baker


class UtilsTest(TestCase):
    def setUp(self):
        self.category_type = baker.prepare('service.CategoryType', name='Test Category 1 name')

    def test_generate_slug(self):
        self.assertEqual(self.category_type.slug, None)
        self.category_type.save()
        self.assertEqual(self.category_type.slug, 'test-category-1-name')

    def test_duplicate_slug(self):
        self.category_type.save()
        category_type2 = baker.make('service.CategoryType', name='Test Category 1 name')
        self.assertNotEqual(self.category_type.slug, category_type2.slug)
