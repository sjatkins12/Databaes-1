# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=False)
    subscribes_to = models.ManyToManyField('Crate.InterestGroup')
    receives = models.ManyToManyField('Crate.Box')

    def __str__(self):
        return self.user.username


class ShippingAddress(models.Model):
    user_id = models.ForeignKey(UserProfile)
    address = models.CharField(primary_key=True, max_length=100)

    # TODO: This does not create address and user_id as the primary keys
    # It guarantees that they are unique so no problems should arise.
    class Meta:
        unique_together = ('user_id', 'address',)
