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
def checkout(request, *args, **kwargs):
    
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    stripe.api_key = stripe_secret_key

    # pk = request.GET.get('pk')
    customer = request.user
    form = CustomerInfoForm()
    basket, created = Basket.objects.get_or_create(customer=customer, completedOrder=False)
    items = basket.basketitems_set.all()
    allBasketItems = basket.get_basket_items
    price = Product.objects.get(id=id)
    print(price)

    if request.method == 'POST':
        form = CustomerInfoForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.creator = request.user
            event = form.save()


            checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price': price,
                    'quantity': 1,
                },
            ],
            mode='payment',
            success_url='/success/',
            cancel_url='/cancel/',
        )
            return redirect(checkout_session.url)
            # return HttpResponseRedirect(reverse('success'))
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