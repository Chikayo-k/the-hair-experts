from django.http import HttpResponse
from .models import Order, OrderItem
from products.models import Product

import json
import time
import stripe

class StripeWebHook:
    """Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic,unknown,unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_succeed(self,event):
        """
        Handle the payment intent succeeded webfook from stripe
        """
        intent = event.data.object
        pid = intent.id
        shopping_bag = intent.metadata.shopping_bag
        save_info = intent.metadata.save_info

        # Get the Charge object
        stripe_charge = stripe.Charge.retrieve(
        intent.latest_charge
        )

        billing_details = stripe_charge.billing_details 
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2) 

         # Clean data in the shipping details
        for field, value in shipping_details.address.items():
            if value == "":
                shipping_details.address[field] = None
        
        order_exists = False
        attempt = 1
        while attempt <=5:
            try:
                order = Order.objects.get(
                    full_name__iexact=shipping_details.name,
                    email__iexact=billing_details.email,
                    phone__iexact=shipping_details.phone,
                    country__iexact=shipping_details.address.country,
                    eircode__iexact=shipping_details.address.postal_code,
                    town_city__iexact=shipping_details.address.city,
                    address1__iexact=shipping_details.address.line1,
                    address2__iexact=shipping_details.address.line2,
                    county_region__iexact=shipping_details.address.state,
                    grand_total=grand_total,
                    original_bag = shopping_bag,
                    stripe_pid = pid,
                )
                order_exists = True
                break               
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
             return HttpResponse(
                content=f'Webhook received: {event['type']} | SUCCESS: The order has already been verified in the database.',
                status=200)
        else: 
            order = None       
            try:            
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    email=billing_details.email,
                    phone=shipping_details.phone,
                    country=shipping_details.address.country,
                    eircode=shipping_details.address.postal_code,
                    town_city=shipping_details.address.city,
                    address1=shipping_details.address.line1,
                    address2=shipping_details.address.line2,
                    county_region=shipping_details.address.state,
                    original_bag = shopping_bag,
                    stripe_pid = pid,
                )
                for item_id, item_data in json.loads(shopping_bag).items():
                    product = Product.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_item = OrderItem(
                            order=order,
                            product=product,
                            quantity=item_data,
                        )
                        order_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(content=f'Webhook received: {event['type']} | ERROR: {e}', status=500)


        return HttpResponse(
            content=f"Webhook received: {event['type']}| SUCCESS: Created order in webhook",
            status=200)
                

    
    def handle_payment_failed(self,event):
        """
        Handle the payment intent failed webfook from stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event['type']}',
            status=200
        )