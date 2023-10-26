from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CustomerProfile(models.Model):
    """
    Table for storing customer address
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    default_phone_number = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    default_street_address1 = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )
    default_street_address2 = models.CharField(
        max_length=80,
        null=False,
        blank=False
    )
    default_town_or_city = models.CharField(
        max_length=40,
        null=False,
        blank=False
    )
    default_lat = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )
    default_postcode = models.CharField(
        max_length=20,
        null=False,
        blank=False
    )
    default_lon = models.CharField(
        max_length=100,
        null=False,
        blank=False
    )

    def __str__(self):
        """
        Override the __str__() to return username
        """
        return self.user.username

