# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length = 15, blank=False)
    last_name = models.CharField(max_length = 15, blank=False)
    address = models.CharField(max_length = 75, blank=False)

    def __str__(self):
        return self.user.username
