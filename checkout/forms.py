from django import forms
from .models import Orders


class OrderForm(forms.ModelForm):
    class Meta:
        model = Orders
        fields = ('full_name', 'email_address', 'phone_number',
                  'street_address1', 'street_address2',
                   'city_or_town', 'postcode', 'country',
                   'county',)

    def __init__(self, *args, **kwargs):
        """
        Adding placeholders and classes, removing auto-generated labels
        and seeting autofocus on the first field.
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
            'email_address': 'Email Address',
            'phone_number': 'Phone Number',
            'country': 'Country',
            'postcode': 'Post Code',
            'city_or_town': 'City or Town',
            'street_address1': 'Street Address 1',
            'street_address2': 'Street Address 2',
            'county': 'County',
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