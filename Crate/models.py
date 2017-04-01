from django.db import models


# Create your models here.

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
    type = models.ForeignKey('hierarchy.InterestGroup', models.CASCADE)
    sold_during = models.ForeignKey(SellingCycle, models.CASCADE)
