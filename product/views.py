from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from product.models import Product
from product.serializers import ProductSerialize
from .forms import ProductForm
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class AllProducts(APIView):
    def get(self, request, *args, **kwargs):
        print("BKM AllProducts get ")
        products = Product.objects.all()
        print("BKM AllProducts get ",products )
        serialized_products = ProductSerialize(products, many=True)
        return Response(serialized_products.data,status=status.HTTP_200_OK)

def get_all_products(request):
    products = Product.objects.all()
    return products

def add_product(request):

    if request.method == 'GET':
        productForm = ProductForm()
        products = Product.objects.all()
        context = {
            'form':productForm,
            'products':products
        }
        return render(request,"product/product.html",context)
    else:
        productForm = ProductForm(request.POST,request.FILES)
        if productForm.is_valid:
            product = productForm.save()
            messages.success(request, "Successfully added product!")
            return redirect("add_product")

def delete_product(request,product_id):

    product = get_object_or_404(Product,pk=product_id)
    product.delete()
    messages.success(request,f"Product Deleted")
    return redirect("add_product")