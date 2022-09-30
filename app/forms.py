from allauth.account.forms import SignupForm
from django import forms
from django.forms import ModelForm
from .models import NewsletterSignup, CustomerInfo

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label='First Name')
    last_name = forms.CharField(max_length=30, label='Last Name')
    def signup(self, request, user):
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

class NewsletterSignupForm(forms.ModelForm):
    class Meta:
        model = NewsletterSignup
        fields = ['email']
        
        def cleanEmail(self):
            email = self.cleaned_data.get('email')

            return email

class CustomerInfoForm(ModelForm):
    class Meta:
        model = CustomerInfo
        fields = [
            'user',
            'company',
            'street_address2',
            'town_or_city',
            'county',
            'country',
            'postcode',
            'phone_number',
            'info'
            ]
