from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework import permissions,status
from rest_framework.response import Response

from checkout.models import Order
from checkout.serializers import OrderSerializer

# Create your views here.

class CustomerOrders(APIView):
    permission_classes = [permissions.IsAuthenticated]
    print("----------BKM-----CustomerOrders-------")
    
    def get(self, request, *args, **kwargs):
        orders = get_object_or_404(Order, email = request.GET['email'])
        serialized_orders = OrderSerializer(orders,many = True)
        return Response(serialized_orders.data,status=status.HTTP_200_OK)