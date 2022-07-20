from django.contrib import admin
from .models import *

# admin.site.register(UserShoppingID)
admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(BasketItems)
admin.site.register(DeliveryAddress)
admin.site.register(Categories)