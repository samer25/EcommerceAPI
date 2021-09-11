from django.urls import path

from products.views import CategoryApiListView, CategoryApiCreateView, CategoryApiRetrieveView

urlpatterns = [
    path('category/', CategoryApiListView.as_view(), name='category'),
    path('category/<slug:slug>/', CategoryApiRetrieveView.as_view(), name='category-retrieve'),
    path('category/create/', CategoryApiCreateView.as_view(), name='category-create'),
]
