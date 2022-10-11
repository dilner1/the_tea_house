from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# from products.models import Product
# from basket.models import Basket

# class BasketItems(models.Model):
#     item = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
#     order = models.ForeignKey(Basket, on_delete=models.SET_NULL, blank=True, null=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     added_date = models.DateTimeField(auto_now_add=True, max_length=150)

#     @property
#     def add_total(self):
#         total = self.item.price * self.quantity
#         return total

class NewsletterSignup(models.Model):
    email = models.EmailField()
    date_added = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.email
