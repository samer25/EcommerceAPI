from django.urls import resolve, reverse
from django.test import TestCase

from products.views import ProductsView, search_products, ProductsByCategoryView, ProductsDetail


class ProductsUrlApiViewTest(TestCase):

    def test_url_products_class_view_should_return_equal(self):
        found = reverse('products')
        self.assertEqual(resolve(found).func.view_class, ProductsView)

    def test_url_products_search_function_view_should_return_equal(self):
        found = reverse('search')
        self.assertEqual(resolve(found).func, search_products)

    def test_url_products_category_slug_class_view_should_return_equal(self):
        found = reverse('category', args=['category_slug'])
        self.assertEqual(resolve(found).func.view_class, ProductsByCategoryView)

    def test_url_products_detail_with_category_slug_and_product_slug_class_view_should_return_equal(self):
        found = reverse('product-detail', args=['category_slug', 'product_slug'])
        self.assertEqual(resolve(found).func.view_class, ProductsDetail)
