from django.contrib import admin
from .models import *


class NeswletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added', )

admin.site.register(Product)
admin.site.register(Basket)
admin.site.register(BasketItems)
admin.site.register(Categories)
admin.site.register(CustomerInfo)
admin.site.register(NewsletterSignup, NeswletterAdmin)