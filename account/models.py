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
    # id (auto-generated) will act as the primary key
    user_id = models.ForeignKey(UserProfile)
    address = models.CharField(max_length=100)

    # This will guarantee that the two columns are unique together
    class Meta:
        unique_together = ('user_id', 'address',)


class Discussion(models.Model):
    discussion_id = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    interest_id = models.ForeignKey('Crate.InterestGroup', on_delete=models.CASCADE)
