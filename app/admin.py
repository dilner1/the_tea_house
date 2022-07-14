from django.contrib import admin
from .models import *

admin.site.register(UserDetail )
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(BasketOrderItems)
admin.site.register(DeliveryAddress)