from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.

def checkout(request):
    shopping_bag = request.session.get('shopping_bag',{})
    if not shopping_bag:
        messages.error(request, "No items in your shopping bag")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context ={
        'order_form':order_form,
        'stripe_public_key': 'STRIPE_PUBLIC',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)

