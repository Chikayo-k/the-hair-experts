from decimal import Decimal
from django.conf import settings

def shopping_bag_contents(request):

    bag_items = []
    total= 0
    product_count= 0
    free_delivery_price = settings.FREE_DELIVERY_PRICE

    if total >= settings.FREE_DELIVERY_PRICE:
        delivery_cost = 0
        
    elif total >= 1 & total < settings.FREE_DELIVERY_PRICE:
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