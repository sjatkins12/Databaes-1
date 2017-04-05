from django import forms
from registration.forms import RegistrationFormUniqueEmail
# from django.contrib.auth.models import User
from account.models import UserProfile

# Form for creating a new user
class UserRegistrationForm(RegistrationFormUniqueEmail):
    first_name = forms.CharField()
    last_name = forms.CharField()
    address = forms.CharField()