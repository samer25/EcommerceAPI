from django.urls import path

from products.views import CategoryViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('category', CategoryViewSet, basename='user')
urlpatterns = router.urls


