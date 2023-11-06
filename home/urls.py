from django.contrib import admin
from django.urls import path
from . import views
from cart.views import calculate_estimatedtime

urlpatterns = [
    path('', views.home, name="home"),
#     path('orderlist', views.view_all_orders, name="orderlist"),
    path('orderlist', calculate_estimatedtime, name="orderlist"),
]