from django.shortcuts import get_object_or_404, render
from .models import Cart
from django.db.models import Count
from product.models import Product

# Create your views here.
def add_to_cart(request):
    cart = Cart.objects.create()
    cart.product = request.POST.get('product')
    cart.email = request.POST.get('email')
    cart.save()

def delete_cart_item(request,cart_id):
    cart = get_object_or_404(Cart,pk=cart_id,email= request.POST.get('email'))
    cart.delete()

def get_all_carts(request):

    productList = {}
    results = Cart.objects.filter(email=request.get('email')).values('product').annotate(quantity=Count('product')).order_by(Product.pk)
    print("get_all_carts =", results)
    for result in results:
        for key in result:
            productList[key]= result[key]
    print("get_all_carts  productList =", productList)

def calculate_estimatedtime(request):
   url= "https://api.nextbillion.io/distancematrix/json?origins=34.05456317,-118.31528428|33.99167000,-118.25687955|34.00792776,-118.33063151&destinations=33.96763110,-118.23215346|33.93969502,-118.26583210|33.90184293,-118.19634326&mode=car&key=<your_api_key>&avoid=highway"
   