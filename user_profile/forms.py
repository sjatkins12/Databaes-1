from django import forms

import account.forms

from django.utils.translation import ugettext_lazy as _

class SignupForm(account.forms.SignupForm):

    first_name = forms.CharField(label=_(u'First name'),
        max_length=30,
        required=True)

    last_name = forms.CharField(label=_(u'Last name'),
        max_length=30,
        required=True)
        
    address = forms.CharField(
        max_length=100,
        required=True)
    
    field_order=['username', 'first_name', 'last_name',
                'email', 'password', 'password_confirm', 'address', ]