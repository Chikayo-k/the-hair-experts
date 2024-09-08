from djangp import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('full_name','email','phone','address1','address2','town_city','county_region',)

    super().__init__(*args,**kwargs)
    placeholders ={
        'full_name': 'Full Name',
        'email':' Email ',
        'phone':' Phone Number',
        'address1': 'Address 1',
        'address2': 'Address 2',
        'town_city': 'Town / City',
        'county_region': 'County /Region',
    }

    self.fields['full_name'].widget.attrs['autofocus'] = True
    for field in self.fields:
        if self.fields[field].required:
            placeholder = f'{placeholders[field]} *'
        else:
            placeholder = placeholders[field]
        self.fields[field].widget.attrs['placeholder'] = placeholder
        self.fields[field].widget.attrs['class'] = 'stripe-style-input'
        self.fields[field].label = False
    