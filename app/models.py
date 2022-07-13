from django.db import models
from django.contrib.auth.models import User

class UserDetails(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.name

class Product(models.Model):
    name = models.CharField(max_length=50, null=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    price = models.FloatField()
    info = models.TextField()
    image = models.ImageField()
    
    def __str__(self):
        return self.name

class Basket(models.Model):
    userDetail = models.ForeignKey(UserDetail, on_delete=models.SET_NULL, blank=True, null=True)
    order_number = models.CharField(max_length=30, null=False, editable=False)
    order_date = models.DateTimeField(auto_now_add=True,)
    completedOrder = models.BooleanField(default=False, Null=True, blank=False)

    def __str__(self):
        return str(self.order_number)

class OrderItems(models.Model):
    item = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
    order = models.ForeignKey(Basket, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True,)