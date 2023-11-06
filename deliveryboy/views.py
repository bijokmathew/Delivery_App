from django.shortcuts import render
from checkout.models import Order
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status
from rest_framework.response import Response

from deliveryboy.serializers import CartSerializer

# Create your views here.

class GetDelivery(APIView):
    permission_classes = [permissions.IsAuthenticated]
    print("BKM   GetDelivery call view")
    def get(self,request,email, *args, **kwargs):
        delivery = Order.objects.filter(delivery_email=email,status="Assigned").order_by("id")
        serializer = CartSerializer(delivery, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
def get_delivery(requset):

    delivery = Order.objects.filter(delivery_email=requset.POST.get('email'),status="Assigned").order_by("id")
    return delivery

def update_order_status(request,status):
    order = Order.objects.get(id=request.POST.get('order_id'))
    order.status = status
    order.save()
    return 'success'

def update_order_delivered(request):
    return update_order_status(request,"Delivered")

def update_order_undelivered(request):
    return update_order_delivered(request,"Not Delivered")