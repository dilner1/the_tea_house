from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404, handler500
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('tea-store/', include('products.urls')),
    path('basket/', include('basket.urls')),
    path('checkout/', include('checkout.urls')),
    path('my-account/', views.NewsletterSignupView, name='my-account'),
    ]

handler404 = "app.views.handler404View"