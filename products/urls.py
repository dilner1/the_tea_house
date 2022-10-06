from django.urls import path
from . import views

urlpatterns = [ 
    path('pots-and-sets-store/', views.potsStore, name='pots-and-sets-store'),
    path('teaware-store/', views.teawareStore, name='teaware-store'),
    path('', views.teaStore, name='tea-store'),    
]