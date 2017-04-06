from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20, primary_key=True)


class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=30, primary_key=True)
    category_name = models.ForeignKey(Category)


class InterestGroup(models.Model):
    interest_id = models.IntegerField(primary_key=True)
    interest_group_name = models.CharField(max_length=30)
    subscription_cost = models.DecimalField(max_digits=6, decimal_places=2)
    subcategory_name = models.ForeignKey(SubCategory)
    have = models.ManyToManyField('Crate.Item')


class SellingCycle(models.Model):
    cycle_date = models.DateField(primary_key=True)


class Box(models.Model):
    """
    Fields-
    1. id = models.AutoField(primary_key=True) is created by default
    2. 4 Foreign Keys to the Tables
    models.ForeignKey(<Model>, on_delete=models.ON_CASCADE)
    Relationships-
    1. Many to Many with User
    2. Many to One with Selling Cycle
    3. Many to Many with Items
    4. Many to One with Interest Groups
    """
    box_id = models.IntegerField(primary_key=True)
    type = models.ForeignKey(InterestGroup)
    sold_during = models.ForeignKey(SellingCycle)


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
    contained_in = models.ManyToManyField(Box)
    sold_in = models.ManyToManyField(SellingCycle)
    sold_by = models.ManyToManyField('inventory.Supplier', through='inventory.SellingOrder')
