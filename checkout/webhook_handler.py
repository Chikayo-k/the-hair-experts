from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings

from .models import Order, OrderItem
from products.models import Product
from profiles.models import UserProfile

import json
import time
import stripe


class StripeWebHook:
    """Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """
       Send a confirmation email when the user purchases
        """
        customised_email = order.email
        subject = render_to_string(
            'checkout/confirmation_email/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_email/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [customised_email]
        )

    def handle_event(self, event):
        """
        Handle a generic,unknown,unexpected webhook event
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)

    def handle_payment_succeed(self, event):
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

        # Update profile info if save info was checked
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone = shipping_details.phone
                profile.default_country = shipping_details.address.country
                profile.default_eircode = shipping_details.address.postal_code
                profile.default_town_city = shipping_details.address.city
                profile.default_address1 = shipping_details.address.line1
                profile.default_address2 = shipping_details.address.line2
                profile.default_county_region = shipping_details.address.state
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
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
                    original_bag=shopping_bag,
                    stripe_pid=pid,
                )
                order_exists = True
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            self._send_confirmation_email(order)
            return HttpResponse(
                 content=f"Webhook received: {event['type']} | SUCCESS: The order has already been verified in the database.", # noqa
                 status=200)
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=shipping_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone=shipping_details.phone,
                    country=shipping_details.address.country,
                    eircode=shipping_details.address.postal_code,
                    town_city=shipping_details.address.city,
                    address1=shipping_details.address.line1,
                    address2=shipping_details.address.line2,
                    county_region=shipping_details.address.state,
                    original_bag=shopping_bag,
                    stripe_pid=pid,
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
                return HttpResponse(content=f"Webhook received: {event['type']} | ERROR: {e}", status=500) # noqa

        self._send_confirmation_email(order)
        return HttpResponse(
            content=f"Webhook received: {event['type']}| SUCCESS: Created order in webhook", # noqa
            status=200)

    def handle_payment_failed(self, event):
        """
        Handle the payment intent failed webfook from stripe
        """
        return HttpResponse(
            content=f"Webhook received: {event['type']}",
            status=200
        )
