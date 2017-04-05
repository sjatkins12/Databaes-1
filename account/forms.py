from django import forms
from registration.forms import RegistrationFormUniqueEmail
from django.contrib.auth.models import User
from account.models import UserProfile

# Form for creating a new user
class UserRegistrationForm(RegistrationFormUniqueEmail):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('address',) 