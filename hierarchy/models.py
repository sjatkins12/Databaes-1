from django.db import models


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=20, primary_key=True)


class SubCategory(models.Model):
    subcategory_name = models.CharField(max_length=30, primary_key=True)


class InterestGroup(models.Model):
    interest_group_name = models.CharField(max_length=30)
    subscription_cost = models.DecimalField(max_digits=6, decimal_places=2)
