from django.contrib import admin
from .models import BasketItems, CustomerInfo

# Register your models here.
admin.site.register(BasketItems)
admin.site.register(CustomerInfo)
