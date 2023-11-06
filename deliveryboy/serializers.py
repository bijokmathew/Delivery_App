from rest_framework import serializers
from django.contrib.auth.models import User
from cart.models import Cart
from product.models import Product

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ["product","email",'date'] 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["name","description","image","price","date_added",]