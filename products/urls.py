from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from products.views import ProductsByCategoryView, ProductsView, ProductsDetail, search_products

urlpatterns = [
    path('products/', ProductsView.as_view()),
    path('products/search/', search_products),
    path('products/<slug:category_slug>/', ProductsByCategoryView.as_view()),
    path('products/<slug:category_slug>/<slug:product_slug>/', ProductsDetail.as_view()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
