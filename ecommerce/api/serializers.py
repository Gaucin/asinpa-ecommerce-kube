from rest_framework import serializers

from ecommerce.models import Order, OrderDetail


class OrderSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Order
        fields = (
            "customer", "employee", "shipper", "order_date",
        )


class OrderDetailSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderDetail
        fields = (
            "product", "quantity",
        )
