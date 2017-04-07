# Create your models here.
from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    """
    Fields-
    1. user- Holds a 1-1 relationship with predefine auth_user model
            - It already stores info like: email, username, password
            firstname, lastname, etc.
    2. address- User's address
    3. Foreign Keys:
    Relationships-
    1. Many to Many with Interest Group                 --In This Model
    2. Many to Many with Box                            --In This Model
    3. One to Many with Discussion                      --In 'Discussion' Model
    4. One to Many with Credit Card                     --Not completed yet
    5. One to Many with Shipping Address                --In 'ShippingAddress' Model
    """
    # TODO: Create a 'through' field for subscribes_to (new model) to represent the attributes in the relationship
    # User <- Many to Many -> Interest_Group has two fields on the relationship
    # Attributes: 1. start_date, 2. end_date
    # TODO: Create a 'through' field for receives (new model) to represent the attribute in the relationship
    # User <- Many to Many-> Box
    # Attributes 1. Report
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255, blank=False)
    subscribes_to = models.ManyToManyField('Crate.InterestGroup')
    receives = models.ManyToManyField('Crate.Box')

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


class CreditCard(models.Model):
    cc_number = models.CharField(primary_key=True, max_length=20)
    username = models.ForeignKey(UserProfile)
    type = models.CharField(max_length=20)
    csv = models.CharField(max_length=4)
    expiration_date = models.CharField(max_length=6)
    billing_address = models.CharField(max_length=100)

    class Meta:
        unique_together = ('cc_number', 'username',)
