from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        """
        Insert placeholders and apply classes
        while removing automatically generated content.
        place labels and make first field autofocus
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'default_phone': ' Phone',
            'default_address1': 'Address 1',
            'default_address2': 'Address 2',
            'default_town_city': 'Town / City',
            'default_county_region': 'County /Region',
            'default_eircode': 'Eir Code',
            'default_country': 'Country',
        }

        self.fields['default_phone'].widget.attrs['autofocus'] = True
        for field in self.fields:
            if field != 'default_country':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].widget.attrs['class'] = 'border-black rounded-0 profile-form-input' # noqa
            self.fields[field].label = False
