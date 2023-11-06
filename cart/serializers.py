from rest_framework import serializers
from django.contrib.auth.models import User
from cart.models import Cart
from checkout.models import Order
from product.models import Product

class EstimateTimeSerializer(serializers.Serializer):
    distance = serializers.IntegerField()
    duration = serializers.IntegerField()

