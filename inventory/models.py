from django.db import models


# Create your models here.
class Supplier(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    supplier_name = models.CharField(max_length=40)
    point_of_contact = models.CharField(max_length=40)


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    date_ordered = models.DateField()
    date_fulfilled = models.DateField()
    order_quantity = models.IntegerField(default=0)


class SellingOrder(models.Model):
    supplier = models.ForeignKey(Supplier)
    order = models.ForeignKey(Order)
    item = models.ForeignKey('item.Item')
