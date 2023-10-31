from django.shortcuts import render
from checkout.models import Order

# Create your views here.

def get_delivery(requset):

    delivery = Order.objects.filter(delivery_email=requset.POST.get('email'),status="Assigned").order_by("id")
    return delivery

def update_order_status(request,status):
    order = Order.objects.get(id=request.POST.get('order_id'))
    order.status = status
    order.save()
    return 'success'

def update_order_delivered(request):
    return update_order_delivered(request,"Delivered")

def update_order_undelivered(request):
    return update_order_delivered(request,"Not Delivered")