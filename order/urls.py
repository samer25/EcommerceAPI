from django.urls import path

from order.views import OrderView, AddToCard

urlpatterns = [
    path('', OrderView.as_view()),
    path('add-to-cart/<slug:product_slug>/', AddToCard.as_view())
]
