from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from order.models import Order, OrderItem
from order.serializer import OrderSerializer
from products.models import ProductModel


class OrderView(APIView):
    def get(self, request):
        queryset = Order.objects.all()
        serializer = OrderSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


class AddToCard(APIView):
    def post(self, request, **kwargs):
        slug = self.kwargs.get('product_slug')
        product = ProductModel.objects.get(slug=slug)
        order, create = Order.objects.get_or_create(user=request.user, complete_order=False)
        order_item_qs = OrderItem.objects.filter(product=product, order=order)
        if order_item_qs.exists():
            order_item = OrderItem.objects.get(product=product, order=order)
            order_item.quantity += 1
            order_item.save()
            return Response(status=status.HTTP_200_OK)
        else:
            order_item = OrderItem.objects.create(product=product, order=order)
            order_item.save()
            return Response(status=status.HTTP_201_CREATED)

