from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.http import HttpResponse
from checkout.models import Order
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    print("home")
    if not request.user.is_superuser:
      return reverse("account_login")
    else:

      if request.method == 'POST': 
         
        print("assign_delivery")
        order = Order.objects.get(order_number=request.POST.get('order_id'))
        order.delivery_email = request.POST.get('divery_boy_email')
        order.status = "Assigned"
        order.save()
          
      orders = Order.objects.filter(status = "open")
      delivery_boys = User.objects.filter(is_staff=True)
      context = {
        'orders': orders,
        'delivery_boys': delivery_boys
      }
      return render(request,'home/index.html',context=context)
  
def view_all_orders(request):
   orders = Order.objects.all()
   context = {
      'orders':orders
   }
   return render(request,'home/list_orders.html',context)