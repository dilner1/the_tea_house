from django.contrib import admin
from django.urls import path, include
from . import views 

from . import views
urlpatterns = [
    path('', views.index, name='Home'),
    path('tea-store/', views.teaStore, name='teaStore'),
    path('pots-store/', views.potsStore, name='potsStore'),
    path('sets-store/', views.setsStore, name='setsStore'),
    path('basket/', views.basket, name='basket'),
    path('checkout/', views.checkout, name='checkout'),
    ]