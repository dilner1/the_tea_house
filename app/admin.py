from django.contrib import admin
from .models import *

admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(BasketItems)
admin.site.register(Categories)
admin.site.register(CustomerInfo)