from django.contrib import admin
from django.urls import path, include
from . import views 

urlpatterns = [
    path('', views.index, name='home'),
    path('tea-store/', views.teaStore, name='tea-store'),
    path('pots-and-sets-store/', views.potsStore, name='pots-and-sets-store'),
    path('teaware-store/', views.teawareStore, name='teaware-store'),
    path('basket/', views.basket, name='basket'),
    path('checkout/', views.checkout, name='checkout'),
    path('update-basket/', views.updateBasket, name='update-basket'),
    path('create-checkout-session/', views.createCheckoutSessionView.as_view(), name='create-checkout-session'),
    path('success/', views.successView, name='success'),
    path('cancel/', views.cancelView, name='cancel'),
    path('my-account/', views.NewsletterSignupView, name='my-account'),
    # path('account/', views.newsletterUnsubscribe, name='account'),
    ]