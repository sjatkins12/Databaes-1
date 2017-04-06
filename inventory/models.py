from django.db import models


# Create your models here.
class Supplier(models.Model):
    supplier_id = models.IntegerField(primary_key=True)
    supplier_name = models.CharField(max_length=40)
    point_of_contact = models.CharField(max_length=40)

    def __str__(self):
        return '{} {}'.format(self.supplier_id, self.supplier_name)


class Order(models.Model):
    order_id = models.IntegerField(primary_key=True)
    date_ordered = models.DateField()
    date_fulfilled = models.DateField()
    order_quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.order_id


class SellingOrder(models.Model):
    supplier = models.ForeignKey(Supplier)
    order = models.ForeignKey(Order)
    item = models.ForeignKey('Crate.Item')

    def __str__(self):
        return '{} {} {}'.format(self.supplier, self.order, self.item)
