from rest_framework import serializers

from order.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'order', 'quantity', 'date_added', 'get_total']


class OrderSerializer(serializers.ModelSerializer):
    order_item = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['id', 'user', 'slug', 'complete_order', 'transaction_id',
                  'date_order', 'get_cart_total', 'get_cart_items', 'order_item']
