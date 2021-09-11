from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from products.views import CategoryViewSet, ProductViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='category')
router.register('', ProductViewSet, basename='products-view')
urlpatterns = router.urls
urlpatterns += [
    path('<slug:category_slug>/<slug:product_slug>/', ProductViewSet.as_view({'get': 'retrieve'}))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
