from rest_framework import serializers

from products.models import Product, Category


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = (
            "name", "category", "unit", "price",
        )
