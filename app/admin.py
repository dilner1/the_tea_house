from django.contrib import admin
from .models import *

admin.site.register(UserDetail)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(BasketOrderItem)
admin.site.register(DeliveryAddress)