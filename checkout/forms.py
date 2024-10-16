from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name', 'email', 'phone', 'address1',
                  'address2', 'town_city', 'county_region',
                  'country', 'eircode', )

    def __init__(self, *args, **kwargs):
        """
        Insert placeholders and apply classes
        while removing automatically generated content.
        place labels and make first field autofocus
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email': ' Email ',
            'phone': ' Phone',
            'address1': 'Address 1',
            'address2': 'Address 2',
            'town_city': 'Town / City',
            'county_region': 'County /Region',
            'eircode': 'Eir Code'
        }

        self.fields['full_name'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'stripe-style-input'
            self.fields[field].label = False
