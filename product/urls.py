from django.urls import path, include
from . import views

urlpatterns = [
    
    path('',views.add_product,name ="add_product" ),
    path('delete/<int:product_id>',views.delete_product,name ="delete_product" ),
     path('user/allproducts',views.get_all_products,name ="all_products" )
]