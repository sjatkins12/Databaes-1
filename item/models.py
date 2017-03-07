from django.db import models


# Create your models here.

class Item(models.Model):
    """
    Fields-
    1. id = models.AutoField(primary_key=True) is created by default
    2. Two Foreign Keys
    Relationships-
    Many to Many with Interest Group
    Many to Many with Box
    Ternary Relationship with Supplier and Orders
    Many to Many with Selling Cycle
    """
    item_name = models.CharField(max_length=40)
    item_description = models.CharField(max_length=500)
    item_quantity = models.IntegerField(default=0)
    price_per_item = models.DecimalField(max_digits=6, decimal_places=2)
    # TODO: Need Supplier ID and Interest ID
