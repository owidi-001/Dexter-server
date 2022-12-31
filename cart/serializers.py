from cart.models import Cart
from products.serializers import ProductSerializer
from rest_framework import serializers

class CartSerializer(serializers.ModelSerializer):
    item=ProductSerializer()

    class Meta:
        model=Cart
        fields=["item","quantity","minQuantity","date_sold"]