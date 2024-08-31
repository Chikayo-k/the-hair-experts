from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product

def shopping_bag_contents(request):

    bag_items = []
    total= 0
    product_count= 0
    delivery_cost = settings.STANDARD_DELIVERY_PRICE
    free_delivery_price = settings.FREE_DELIVERY_PRICE
    free_delivery_cost = 50
    shopping_bag = request.session.get('shopping_bag', {})
    

    for item_id, quantity in shopping_bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price 
        product_count += quantity
        bag_items.append({
            'item_id':item_id,
            'quantity':quantity,
            'product':product,
        }) 

    if total >= settings.FREE_DELIVERY_PRICE:
        delivery_cost = 0
        
    elif total >= 1 and total < settings.FREE_DELIVERY_PRICE:
        delivery_cost =settings.STANDARD_DELIVERY_PRICE 
        free_delivery_cost =  free_delivery_price - total
    else:
       free_delivery_cost =  free_delivery_price - total 

    grand_total = delivery_cost + total
    
    context={
        'bag_items':bag_items,
        'total':total,
        'product_count':product_count,
        'delivery_cost':delivery_cost,
        'free_delivery_cost':free_delivery_cost,
        'grand_total':grand_total,
    }
    
    return context







