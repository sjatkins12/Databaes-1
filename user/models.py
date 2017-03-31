from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(max_length=40, unique=True)
    subscribes_to = models.ManyToManyField('hierarchy.InterestGroup')
    receives = models.ManyToManyField('Crate.Box')


# Weak Entities models based on: https://stackoverflow.com/questions/22577060/weak-entities-in-django
# Was having the issue of old creating a hidden id primary key --maybe this solves it
class ShippingAddress(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)

    class Meta:
        unique_together = ('username', 'address')


class CreditCard(models.Model):
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    cc_number = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    csv = models.CharField(max_length=4)
    expiration_date = models.CharField(max_length=6)
    billing_address = models.CharField(max_length=100)

    class Meta:
        unique_together = ('username', 'cc_number')
