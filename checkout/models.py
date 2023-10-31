from django.db import models
from profiles.models import CustomerProfile
from product.models import Product

# Create your models here.
class Order(models.Model):
    """
        Table for customer orders
    """
    order_number = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        editable=False
    )
    product = models.ManyToManyField(Product,related_name='products')

    class OrderStatus(models.TextChoices):
        """
        Defines the contact options
        """
        OPEN = 'Open', 'Order created and not assigned'
        ASSIGNED = 'Assigned', 'Order Assigned for delivery'
        DELIVERED = 'Delivered', 'Order delivered to the customer'
        NOTDELIVERED = 'Not Delivered', 'Order undelivered to the customer'

    status = models.CharField(
        max_length=250,
        choices= OrderStatus.choices,
        default=OrderStatus.OPEN
    )
    user_profile = models.ForeignKey(
        CustomerProfile,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='orders'
    )
    full_name = models.CharField(
        max_length=50,
        null=False,
        blank=False
    )
    email = models.EmailField(
        max_length=254,
        null=False,
        blank=False
    )
    delivery_email = models.EmailField(
        max_length=254,
        null=True,
        blank=True
    )
    phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    status = models.CharField(
        max_length=255,
        null=False,
        blank=False
    )
    postcode = models.CharField(
        max_length=20,
        null=True,
        blank=True
    )
    town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False
    )
    street_address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )
    street_address2 = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )
    address_lat = models.CharField(
        max_length=400,
        null=False,
        blank=False
    )
    address_lon = models.CharField(
        max_length=400,
        null=False,
        blank=False
    )

    order_date = models.DateField(
        auto_now_add=True,
        editable=False
    )
    
    order_update_date = models.DateField(
        auto_now=True,
        editable=False
    )