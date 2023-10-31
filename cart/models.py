from django.db import models
from product.models import Product

# Create your models here.

class Cart(models.Model):
    product = models.OneToOneField(Product, related_name='products')
    email = models.EmailField(max_length=1024,blank=False,null=False)
    date = models.DateField(auto_now=True,editable=False)