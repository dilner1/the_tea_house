from django.contrib import admin
from .models import NewsletterSignup


class NeswletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_added',)

admin.site.register(NewsletterSignup, NeswletterAdmin)