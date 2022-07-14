from django.contrib import admin
from .models import UserDetails, Product, Basket, BasketOrderItems, DeliveryAddress,

admin.site.register(UserDetails)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(BasketOrderItems)
admin.site.register(DeliveryAddress)