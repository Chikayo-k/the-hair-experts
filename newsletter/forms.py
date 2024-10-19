from django import forms


class NewsletterForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=128)
