from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from products.models import Product

# Create your views here.

def view_bag(request):
  """A view that renders the bag contents page"""
  return render(request, 'shopping_bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
        messages.success(request, f'{quantity} more {product.name} was added to your bag')
    else:
        shopping_bag[item_id] = quantity
        messages.success(request, f'{product.name} was added to your bag')

    request.session['shopping_bag'] = shopping_bag

    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """ Adjust bag """

    quantity = int(request.POST.get('quantity'))
    quantity = int(request.POST.get('quantity'))
    shopping_bag = request.session.get('shopping_bag', {})
    product = get_object_or_404(Product, pk=item_id)

    if quantity > 0:
        shopping_bag[item_id] = quantity
        messages.success(request, f'{product.name} quantity: {quantity} in your bag')
    else:
        shopping_bag.pop(item_id)
        messages.success(request, f'{product.name} was removed form your bag')

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('view_bag'))


def remove_bag(request, item_id):
    """ Remove items from the bag """
    try:
        product = get_object_or_404(Product, pk=item_id)
        shopping_bag = request.session.get('shopping_bag', {})
        shopping_bag.pop(item_id)
        messages.success(request, f'{product.name} was removed form your bag')
        request.session['shopping_bag'] = shopping_bag
        return HttpResponse(status=200)

    except Exception as e:
        message.error(request, f'Error: {e}')
        return HttpResponse(status=500)

        