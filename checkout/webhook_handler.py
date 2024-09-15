from django.http import HttpResponse


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
        return HttpResponse(
            content=f'Webhook received: {event['type']}',
            status=200
        )
    
    def handle_payment_failed(self,event):
        """
        Handle the payment intent failed webfook from stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event['type']}',
            status=200
        )