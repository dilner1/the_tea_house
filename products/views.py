from app.models import Basket
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def teaStore(request):
    customer = request.user
    basket, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)
    items = basket.basketitems_set.all()
    allBasketItems = basket.get_basket_items

    products = Product.objects.all()
    context = {
        'products':products,
        'allBasketItems':allBasketItems
        }

    return render(request, 'app/tea-store.html', context)

@login_required(login_url='/accounts/login/')
def potsStore(request):

    customer = request.user
    basket, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)
    items = basket.basketitems_set.all()
    allBasketItems = basket.get_basket_items

    products = Product.objects.all()
    context = {
        'products':products,
        'allBasketItems':allBasketItems
        }

    return render(request, 'app/pots-and-sets-store.html', context)

@login_required(login_url='/accounts/login/')
def teawareStore(request):
    customer = request.user
    basket, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)
    items = basket.basketitems_set.all()
    allBasketItems = basket.get_basket_items

    products = Product.objects.all()
    context = {
        'products':products,
        'allBasketItems':allBasketItems
        }
    return render(request, 'app/teaware-store.html', context)