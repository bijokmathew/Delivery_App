from django.shortcuts import get_object_or_404, render
import requests
from cart.forms import OrderForm
from cart.serializers import EstimateTimeSerializer

from checkout.models import Order
from deliveryboy.serializers import CartSerializer
from .models import Cart
from profiles.models import CustomerProfile
from django.db.models import Count
from product.models import Product
from rest_framework.decorators import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

class CartView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    print("----------BKM-----CartView-------")
    def get_object(self, cart_id, user_email):
        '''
        Helper method to get the object with given todo_id, and user_id
        '''
        try:
            return Cart.objects.get(id=cart_id, email = user_email)
        except Cart.DoesNotExist:
            return None

    def post(self, request, *args, **kwargs):
        data = {
            "product": request.data.get('product'),
            "email": request.data.get('email')
        }
        serilizer = CartSerializer(data=data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(serilizer.data,status=status.HTTP_201_CREATED)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, cart_id,email, *args, **kwargs):
        cart = self.get_object(cart_id,request.user.email)
        if not cart:
            return Response("Cart not exist", status= status.HTTP_400_BAD_REQUEST)
        cart.delete()
        return Response("Cart deleted", status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
       print("get ------------")
       #allCarts = get_object_or_404(Cart,email=request.user.email) 
       allCarts =""
       allCartserializer = CartSerializer(allCarts,many=True)
       profile = CustomerProfile.objects.filter(user=request.user)
       estimatedtime= calculate_estimatedtime(request,profile)
       print("estimatedtime =",estimatedtime )
       print("estimatedtime list =",[estimatedtime] )
       estimatedtimeSerialized = EstimateTimeSerializer([estimatedtime],many=True)
       data = estimatedtimeSerialized.data + allCartserializer.data 
       return Response(data,status=status.HTTP_200_OK)

class ConfirmOrder(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        cart = Cart.objects.filter(email=requests.GET['email'])
        if not cart:
            statumsg = "Cart is Empty"
            
        else:
            profile = CustomerProfile.objects.filter(user=request.user)
            order = OrderForm(request.POST)
            if order.is_valid():
                order.save(commit=False)
                order.user_profile = profile
                order.status = "Open"
                order.save()
                statumsg = "Order done"
        return Response(statumsg, status=status.HTTP_200_OK)

class ClearAllCart(APIView):
    def delete(self, request,email, *args, **kwargs):
        cart = self.get_object(request.user.email)
        if not cart:
            return Response("Cart not exist", status= status.HTTP_400_BAD_REQUEST)
        cart.delete()
        return Response("All Cart deleted", status=status.HTTP_200_OK)

def get_all_carts(request):

    productList = {}
    results = Cart.objects.filter(email=request.get('email')).values('product').annotate(quantity=Count('product')).order_by(Product.pk)
    print("get_all_carts =", results)
    for result in results:
        for key in result:
            productList[key]= result[key]
    print("get_all_carts  productList =", productList)

def calculate_estimatedtime(request,profile):
   dist_duration = {}
   source_lon=10.0274266
   source_lat=76.3058943
   #{{profile.default_lat}},{{profile.default_lon}}
  # url= "https://api.nextbillion.io/distancematrix/json?origins=source_lat,source_lon&destinations=10.157270,76.356550&mode=car&key=b98e9dd2f9414231bae19340b76feff0&avoid=highway"
   url = "https://api.nextbillion.io/distancematrix/json?origins=10.0274266,76.3058943&destinations=10.157270,76.356550&mode=car&key=b98e9dd2f9414231bae19340b76feff0&avoid=highway"
   result = requests.get(url)
   print("calculate_estimatedtime  result =", result)
   if result.status_code == 200:
       result_in_json= result.json()
       print("calculate_estimatedtime  result_in_json =", result_in_json)
       dist_duration['distance']= result_in_json['rows'][0]["elements"][0]['distance']['value']
       dist_duration['duration']= result_in_json['rows'][0]["elements"][0]['duration']['value']
    
   print("calculate_estimatedtime  dist_duration =", dist_duration)
   return dist_duration
    