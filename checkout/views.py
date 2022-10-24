from django.shortcuts import render
# from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.conf import settings

import stripe
from .models import BasketItems, CustomerInfo
from basket.models import Basket
from products.models import Product
from .forms import CustomerInfoForm

# Create your views here.
@login_required(login_url='/accounts/login/')
def checkout(request):
    
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key

    customer = request.user
    form = CustomerInfoForm()
    basket, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)
    items = basket.basketitems_set.all()
    allBasketItems = basket.get_basket_items



    # data = json.loads(request.body)
    # itemId = data['itemId']
    # item = Product.objects.get(id=itemId)


    baseURL = 'https://8000-dilner1-theteahouse-gylthi4t20e.ws-eu72.gitpod.io.loca.lt/'

    if request.method == 'POST':
        form = CustomerInfoForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event = form.save()

            checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[{
                'price_data': {
                    'currency': 'gbp',
                    'product_data': {
                    'name': 'T-shirt',
                    },
                    'unit_amount': 2000,
                },
                'quantity': 1,
                }],
            mode='payment',
            success_url= '/success/',
            cancel_url= '/cancel/',
        )
            context = {
                'items': items,
                'basket': basket,
                'form': form,
                'allBasketItems': allBasketItems,
                'stripe_public_key': stripe_secret_key,
                'client_secret': 'test client secret',
        }

            return render(request, 'app/checkout.html', context)

        else:
            print("ERROR : ", form.errors)
    context = {
        'items': items,
        'basket': basket,
        'form': form,
        'allBasketItems': allBasketItems,
        'stripe_public_key': stripe_secret_key,
        'client_secret': 'test client secret',
        }
    return render(request, 'app/checkout.html', context)


def successView(request):
    context = {}
    return render(request, "app/success.html/", context)

def cancelView(request):
    context={}
    return render(request, "app/cancel.html/", context)