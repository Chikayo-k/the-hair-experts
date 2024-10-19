from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from newsletter.forms import NewsletterForm
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

mailchimp = Client()
mailchimp.set_config({
  'api_key': settings.MAILCHIMP_API_KEY,
  'server': settings.MAILCHIMP_REGION,
})


def mailchimp_ping_view(request):
    response = mailchimp.ping.get()
    return JsonResponse(response)


def subscribe(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            try:
                form_email = form.cleaned_data['email']
                member_info = {
                    'email_address': form_email,
                    'status': 'subscribed',
                }
                response = mailchimp.lists.add_list_member(
                    settings.MAILCHIMP_MARKETING_AUDIENCE_ID,
                    member_info,
                )
                logger.info(f'API call successful: {response}')
                messages.success(request, 'Subscribed successfully!')
                return redirect('subscribe-success')

            except ApiClientError as error:
                logger.error(f'An exception occurred: {error.text}')
                messages.error(request, 'Fail subscribed. Try again!')
                return redirect('subscribe-fail')

    return render(request, 'newsletter/subscribe.html', {
        'form': NewsletterForm(),
    })


def subscribe_success(request):
    return render(request, 'newsletter/message.html', {
        'title': 'Successfully subscribed',
        'message': 'You have successfully subscribed to our mailing list. Keep an eye out for some exciting offers and news about our new products', # noqa
    })


def subscribe_fail(request):
    return render(request, 'newsletter/message.html', {
        'title': 'Failed to subscribe',
        'message': 'Sorry, something went wrong. Please try it again.',
    })
