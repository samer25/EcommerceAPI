from rest_framework import serializers

from products.models import CategoryModel, ProductModel


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryModel
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = ['category', 'title', 'descriptions', 'availability',
                  'price', 'slug', 'date_added', 'get_absolute_url',
                  'get_image', 'get_thumbnail', 'date_added']
