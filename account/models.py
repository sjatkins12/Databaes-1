# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class Subscription(models.Model):
    """
    Fields-
    1. start_date- Date which subscription starts
    2. end_data- Date which subscription ends
    3. Foreign Keys:
    Relationships-
    1. Many to One with Box                             --In This Model
    2. Many to One with UserProfile                     --In This Model
    Note: Foreign Keys are set to 'Protect' so if a reference exists,
    the reference won't be changed to null, so start_date and end_date
    always references to a valid (or non-continuing) interest group
    """
    start_date = models.DateField()
    end_date = models.DateField()
    box_id = models.ForeignKey('Crate.Box', on_delete=models.PROTECT)
    user_id = models.ForeignKey('account.UserProfile', on_delete= models.PROTECT)

    # This guarantees that box_id and user_id are unique (act as primary keys)
    class Meta:
        unique_together = ('box_id', 'user_id')


class Reports(models.Model):
    """
    Fields-
    1. report- String which user records issues with a Box
    2. Foreign Keys:
    Relationships
    1. Many to One with Box                             --In This Model
    2. Many to One with UserProfile                     --In This Model
    Note: Foreign Keys are set to 'Protect' so if a reference exists,
    the reference won't be changed to null, so report will always reference
    a valid box or user
    """
    report = models.CharField(max_length=500)
    box_id = models.ForeignKey('Crate.Box', on_delete=models.PROTECT)
    user_id = models.ForeignKey('account.UserProfile', on_delete=models.PROTECT)

    # This guarantees that box_id and user_id are unique (act as primary keys)
    class Meta:
        unique_together = ('box_id', 'user_id')


class UserProfile(models.Model):
    """
    Fields-
    1. user- Holds a 1-1 relationship with predefine auth_user model
            - It already stores info like: email, username, password
            first name, last name, etc.
    2. address- User's address
    3. Foreign Keys:
    Relationships-
    1. Many to Many with Interest Group                 --In This Model
    2. Many to Many with Box                            --In This Model
    3. One to Many with Discussion                      --In 'Discussion' Model
    4. One to Many with Credit Card                     --Not completed yet
    5. One to Many with Shipping Address                --In 'ShippingAddress' Model
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=False)
    subscribes_to = models.ManyToManyField('Crate.InterestGroup', through='Subscription')
    receives = models.ManyToManyField('Crate.Box', through='Reports')

    def __str__(self):
        return self.user.username


class ShippingAddress(models.Model):
    """
    Fields-
    1. address- Address of the shipping location
    2. Foreign Keys:
    Relationships-
    1. One to Many with UserProfile                     --In This Model
    """
    # id (auto-generated) will act as the primary key
    user_id = models.ForeignKey(UserProfile)
    address = models.CharField(max_length=100)

    # This will guarantee that the two columns are unique together
    class Meta:
        unique_together = ('user_id', 'address',)

    def __str__(self):
        return '{} {}'.format(self.id, self.address)


class Discussion(models.Model):
    """
    Fields-
    1. discussion_id- Identifier for a discussion post
    2. comment- String of user's comment
    3. Foreign Keys:
    Relationships-
    1. One to Many with UserProfile                     --In This Model
    2. One to Many with Discussion                      --In This Model
    """
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    interest_id = models.ForeignKey('Crate.InterestGroup', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.id, self.user)
