from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
# from djangomailchimp import settings
from newsletter.forms import NewsLetterForm
from mailchimp3 import MailChimp
# from mailchimp_v3 import settings


def subscribe(request):
    if request.method == 'POST':
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            form_email = form.cleaned_data['email']
            messages.success(request, 'Subscribed successfully!')
        else:
            messages.error(request, 'Failto subscribed. Try again!')
    return render(request, 'newsletter/subscribe.html', {
        'form': NewsLetterForm(),
    })

