from django import forms
from django.core.validators import RegexValidator
from .models import Listing, Agent, Neighborhood, PropertyType, SaleStatus, PriceRange


class ListingForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = ['address', 'city', 'state', 'zip_code', 'neighborhood', 'property_type', 'sale_status', 'price_range',
                  'price', 'is_featured', 'visibility', 'bedroom_count', 'bathroom_count', 'description', 'photo1',
                  'photo2', 'photo3', 'photo4']
        widgets = {
            'neighborhood': forms.Select(),
            'property_type': forms.Select(),
            'sale_status': forms.Select(),
            'price_range': forms.Select(),
            # Add other fields as needed
        }


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', message="Phone number must be entered in the format: "
                                                               "'+999999999'. Up to 15 digits allowed.")],
        max_length=17,
        required=False  # Set to True if the phone field is mandatory
    )
    message = forms.CharField(widget=forms.Textarea)
