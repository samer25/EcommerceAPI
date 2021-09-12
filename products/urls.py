from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from products.views import ProductsByCategoryView, ProductsView, ProductsDetail, search_products

urlpatterns = [
    path('products/', ProductsView.as_view(), name='products'),
    path('products/search/', search_products, name='search'),
    path('products/<slug:category_slug>/', ProductsByCategoryView.as_view(), name='category'),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductsDetail.as_view(), name='product-detail'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
