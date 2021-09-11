from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response

from products.models import Category
from products.serializer import CategorySerializer


class CategoryApiListView(generics.ListAPIView):
    # permission_classes = []
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryApiCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryApiRetrieveView(generics.RetrieveAPIView):
    # permission_classes = []
    serializer_class = CategorySerializer

    def get_object(self, **kwargs):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Category, slug=slug)
