from django.db import models


# Create your models here.


# TODO: Find potential libraries to use for django payments: https://djangopackages.org/grids/g/payment-processing/
class CreditCard(models.Model):
    # TODO: We should consider using choices for type
    # https://docs.djangoproject.com/en/1.11/ref/models/fields/#django.db.models.Field.choices
    """
    Fields-
    1. cc_number- Credit Card number (String)
    2. type- Type of credit card
    3. CSV- Credit card cc value
    4. expiration_date- Credit card expiration date
    5. billing_address- Credit Card billing address
    6. Foreign Keys:
    Relationship-
    1. username- Many to One with UserProfile                       --In This Model
    """
    cc_number = models.CharField(primary_key=True, max_length=20)
    type = models.CharField(max_length=20)
    csv = models.CharField(max_length=4)
    expiration_date = models.CharField(max_length=6)
    billing_address = models.CharField(max_length=100)
    username = models.ForeignKey('account.UserProfile')

    class Meta:
        unique_together = ('cc_number', 'username',)
