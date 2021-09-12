from django.urls import reverse
from django.utils import timezone
from rest_framework.test import APITestCase

from products.models import ProductModel, CategoryModel


class TestProductViews(APITestCase):

    def setUp(self):
        CategoryModel.objects.create(id=1, name='django', slug='django')
        ProductModel.objects.create(category_id=1, title='Title', descriptions='Des',
                                    price=333.30, image='products/download.jpeg', slug='title',
                                    date_added=timezone.now())

    def test_class_product_view_should_return_200(self):
        url = reverse('products')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_class_product_by_category_should_return_200(self):
        url = reverse('category', args=['django'])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_class_product_by_category_should_return_404(self):
        url = reverse('category', args=['no_exist'])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_class_product_details_should_return_200(self):
        url = reverse('product-detail', args=['django', 'title'])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)

    def test_class_product_details_should_return_400(self):
        url = reverse('product-detail', args=['not_exist', 'not_exist'])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 404)

    def test_function_search_should_return_200(self):
        url = reverse('search')
        data = {
            'query': 'django',
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, 200)

    def test_function_search_should_return_empty_list(self):
        url = reverse('search')
        data = {
            'query': None,
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.data, [])
