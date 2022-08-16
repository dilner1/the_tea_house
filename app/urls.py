from django.contrib import admin
from django.urls import path, include
from . import views 

from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('tea-store/', views.teaStore, name='tea-store'),
    path('pots-and-sets-store/', views.potsStore, name='pots-and-sets-store'),
    path('teaware-store/', views.teawareStore, name='teaware-store'),
    path('basket/', views.basket, name='basket'),
    path('checkout/', views.checkout, name='checkout'),
    path('update-basket/', views.updateBasket, name='update-basket'),
    ]