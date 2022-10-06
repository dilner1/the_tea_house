from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.conf import settings

from products.models import Product
from basketmodels import Basket

class BasketItems(models.Model):
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Basket, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True, max_length=150)

    @property
    def add_total(self):
        total = self.item.price * self.quantity
        return total

class CustomerInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    company = models.CharField(max_length=80, null=False, blank=True)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    county = models.CharField(max_length=80, null=True, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    info = models.TextField(null=True, blank=True)

    # def __str__(self):
    #     return str(self.postcode)

class NewsletterSignup(models.Model):
    email = models.EmailField()
    date_added = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.email
