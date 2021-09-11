from rest_framework import serializers

from products.models import CategoryModel, ProductModel


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['category', 'title', 'descriptions', 'availability',
                  'price', 'slug', 'date_added', 'get_absolute_url',
                  'get_image', 'get_thumbnail', 'date_added']


class CategorySerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True)

    class Meta:
        model = CategoryModel
        fields = ['id', 'name', 'get_absolute_url', 'products']
