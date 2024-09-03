from django.shortcuts import render, redirect, reverse

# Create your views here.

def view_bag(request):
  """A view that renders the bag contents page"""
  return render(request, 'shopping_bag/shopping_bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    shopping_bag = request.session.get('shopping_bag', {})

    if item_id in list(shopping_bag.keys()):
        shopping_bag[item_id] += quantity
    else:
        shopping_bag[item_id] = quantity

    request.session['shopping_bag'] = shopping_bag

    return redirect(redirect_url)

def adjust_bag(request, item_id):
    """ Adjust bag """

    quantity = int(request.POST.get('quantity'))
    shopping_bag = request.session.get('shopping_bag', {})

    if quantity > 0:
        shopping_bag[item_id] = quantity
    else:
        shopping_bag.pop(item_id)

    request.session['shopping_bag'] = shopping_bag
    return redirect(reverse('view_bag'))


# def remove_bag(request, item_id):
#     """ Remove items from the bag """

#     quantity = int(request.POST.get('quantity'))
#     shopping_bag = request.session.get('shopping_bag', {})

#     if quantity > 0:
#         shopping_bag[item_id] = quantity
#     else:
#         shopping_bag.pop[item_id]

#     request.session['shopping_bag'] = shopping_bag
#     return redirect(reverse('view_bag'))