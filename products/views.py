from django.http import Http404
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet

from products.models import CategoryModel, ProductModel
from products.serializer import CategorySerializer, ProductSerializer


class CategoryViewSet(ViewSet):

    def get_permissions(self):
        if self.action == 'create':
            permission_classes = [IsAdminUser]
        else:
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = CategoryModel.objects.all()
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, **kwargs):
        slug = self.kwargs.get('pk')
        category = get_object_or_404(CategoryModel, slug=slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductViewSet(ViewSet):
    def list(self, request):
        queryset = ProductModel.objects.all()
        serializer = ProductSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def get_object(self, category_slug, product_slug):
        try:
            return ProductModel.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except ProductModel.DoesNotExist:
            raise Http404

    def retrieve(self, request, **kwargs):
        category = self.kwargs['category_slug']
        product = self.kwargs['product_slug']
        products = self.get_object(category, product)
        serializer = ProductSerializer(products)
        return Response(serializer.data)
