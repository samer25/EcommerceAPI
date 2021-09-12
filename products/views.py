from django.db.models import Q
from django.http import Http404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from products.models import CategoryModel, ProductModel
from products.serializer import CategorySerializer, ProductSerializer


class ProductsView(APIView):
    def get(self, request):
        queryset = ProductModel.objects.all()
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductsByCategoryView(APIView):

    def get_object(self, category_slug):
        try:
            return CategoryModel.objects.get(slug=category_slug)
        except CategoryModel.DoesNotExist:
            raise Http404

    def get(self, request, **kwargs):
        category_slug = self.kwargs.get('category_slug')
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ProductsDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            return ProductModel.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except ProductModel.DoesNotExist:
            raise Http404

    def get(self, request, **kwargs):

        category_slug = self.kwargs.get('category_slug')
        product_slug = self.kwargs.get('product_slug')
        products = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(products)
        return Response(serializer.data, status.HTTP_200_OK)


@api_view(['POST'])
def search_products(request):
    query = request.data.get('query', '')
    founded_data = []

    if query:
        query_list = query.split(" ")

        for query in query_list:
            product = ProductModel.objects.filter(Q(category__name__icontains=query) | Q(descriptions__icontains=query))
            serializer = ProductSerializer(product, many=True)
            founded_data += serializer.data
        return Response(founded_data, status=status.HTTP_200_OK)
    return Response(founded_data)
