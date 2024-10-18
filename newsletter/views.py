from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
#from djangomailchimp import settings
from newsletter.forms import NewsletterForm
from mailchimp3 import MailChimp
# from mailchimp_v3 import settings
from mailchimp_marketing import Client
from mailchimp_marketing.api_client import ApiClientError
from django.conf import settings



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
            form_email = form.cleaned_data['email']
            messages.success(request, 'Subscribed successfully!')
        else:
            messages.error(request, 'Failto subscribed. Try again!')
    return render(request, 'newsletter/subscribe.html', {
        'form': NewsletterForm(),
    })

