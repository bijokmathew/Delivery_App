from django.db import models

# Create your models here.

class Product(models.Model):
    """
      Product table
    """

    name = models.CharField(
        max_length=254,
        unique=True
    )
    description = models.TextField(
        max_length=1256,
        blank=True,
        null=True
    )
    image = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2
    )
    date_added = models.DateTimeField(
        auto_now_add=True,
        editable=False
    )

    def __str__(self):
        """
        Returns the Product name string
        Args:
            self (object): self.
        Returns:
            The Product name string
        """
        return self.name
