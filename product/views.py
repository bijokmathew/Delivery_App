from django.shortcuts import get_object_or_404, render,redirect
from django.contrib import messages
from product.models import Product
from .forms import ProductForm

# Create your views here.

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