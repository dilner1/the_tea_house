from django.urls import path
from . import views

urlpatterns = [ 
    path('success/', views.successView, name='success'),
    path('cancel/', views.cancelView, name='cancel'),
    path('', views.checkout, name='checkout'),
]