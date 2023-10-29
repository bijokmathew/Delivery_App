from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from checkout.models import Order
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    if not request.user.is_superuser:
      return render(request,'home/index.html')
    else:
       orders = Order.objects.filter(status = "OPEN")
       delivery_boys = User.objects.filter(is_staff=True)
       context = {
        'orders': orders,
        'delivery_boys': delivery_boys
        }
       return render(request,'home/index_admin.html',context=context)