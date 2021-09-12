from django.test import TestCase
from django.utils import timezone

from products.models import CategoryModel, ProductModel


class TestModelCategory(TestCase):

    def setUp(self):
        CategoryModel.objects.create(name='django', slug='django')

    def test_category_model_str_should_return_equal(self):
        category = CategoryModel.objects.get(name='django')
        self.assertEqual(str(category), 'django')

    def test_category_model_get_absolute_url_should_return_equal(self):
        category_absolute_url = CategoryModel.objects.get(name='django').get_absolute_url()
        self.assertEqual(category_absolute_url, '/django/')


class TestModelProducts(TestCase):
    def setUp(self):
        CategoryModel.objects.create(id=1, name='django', slug='django')
        ProductModel.objects.create(category_id=1, title='Title', descriptions='Des',
                                    price=333.30, image='products/download.jpeg', slug='Title',
                                    date_added=timezone.now())

        ProductModel.objects.create(category_id=1, title='Title_no_img', descriptions='Des',
                                    price=333.30, slug='Title',
                                    date_added=timezone.now())
        ProductModel.objects.create(category_id=1, title='Title_with_thumbnail', descriptions='Des',
                                    price=333.30, image='products/download.jpeg', thumbnail='products/download.jpeg',
                                    slug='Title',
                                    date_added=timezone.now())

    def test_product_model_str_should_return_equal(self):
        product = ProductModel.objects.get(title='Title')
        self.assertEqual(str(product), 'Title')

    def test_product_model_get_absolute_url_should_return_equal(self):
        product_absolute_url = ProductModel.objects.get(title='Title').get_absolute_url()
        self.assertEqual(product_absolute_url, '/django/title/')

    def test_product_model_get_image_should_return_true(self):
        product_get_image = ProductModel.objects.get(title='Title').get_image()
        self.assertTrue(product_get_image)

    def test_product_model_get_no_image_should_return_equal(self):
        product = ProductModel.objects.get(title='Title_no_img')
        product_image = product.get_image()
        self.assertEqual(product_image, '')

    def test_product_model_get_thumbnail_should_return_True(self):
        product_get_thumbnail = ProductModel.objects.get(title='Title').get_thumbnail()
        self.assertTrue(product_get_thumbnail)

    def test_product_model_get_thumbnail_if_exist_should_return_True(self):
        product_get_thumbnail = ProductModel.objects.get(title='Title_with_thumbnail').get_thumbnail()
        self.assertTrue(product_get_thumbnail)

    def test_product_model_get_no_thumbnail_should_return_equal(self):
        product = ProductModel.objects.get(title='Title_no_img')
        product_thumbnail = product.get_thumbnail()
        self.assertEqual(product_thumbnail, '')

    def test_product_model_make_thumbnail_thumbnail_should_return_true(self):
        product = ProductModel.objects.get(title='Title')
        ProductModel.make_thumbnail(product, product.image)
        self.assertTrue(product.get_thumbnail())
