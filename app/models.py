from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from django.conf import settings

class Categories(models.Model):
    category = models.CharField(max_length=512)

    def __str__(self):
        return self.category

class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    price = models.FloatField()
    info = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey('Categories', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name

class Basket(models.Model):
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=30, null=False)
    order_date = models.DateTimeField(auto_now_add=True,)
    completedOrder = models.BooleanField(default=False, null=True, blank=False)

    def __str__(self):
        return str(self.id)

class BasketItems(models.Model):
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Basket, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True,)

class CustomerInfo(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)
    customer_order = models.ForeignKey(Basket, on_delete=models.SET_NULL, blank=True, null=True)
    street_address1 = models.CharField(max_length=80, default='Street Address 1', null=False, blank=False)
    street_address2 = models.CharField(max_length=80, default='Street Address 2', null=True, blank=True)
    town_or_city = models.CharField(max_length=40, default='Town or City', null=False, blank=False)
    county = models.CharField(max_length=80, default='County, Province or State', null=True, blank=True)
    country = CountryField(blank_label='Country *', max_length=80, default='Country', null=False, blank=False)
    postcode = models.CharField(max_length=20, default='Post Code', null=True, blank=True)
    phone_number = models.CharField(max_length=20, default='Phone Number', null=False, blank=False)
    info = models.TextField(null=True, blank=True)