from django import forms
from django.forms import ModelForm
from .models import NewsletterSignup, CustomerInfo

class CustomerInfoForm(ModelForm):
    class Meta:
        model = CustomerInfo
        fields = [
            'company',
            'street_address2',
            'town_or_city',
            'county',
            'country',
            'postcode',
            'phone_number',
            'info'
            ]
