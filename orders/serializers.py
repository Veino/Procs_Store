from rest_framework import serializers
from .models import Order, OrderItem, Shipping_Address

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = [
            "product",
            "order",
            "quantity",
        ]

class OrderSerializer(serializers.ModelSerializer):

    OrderItems = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = "__all__"

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping_Address
        fields = "__all__"