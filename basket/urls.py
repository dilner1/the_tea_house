from django.urls import path
from . import views

urlpatterns = [ 
    path('update-basket/', views.updateBasket, name='update-basket'),
    path('', views.basket, name='basket'),    
]
