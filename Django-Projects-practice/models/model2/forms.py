from django import forms
from .models import Product

class Add_product(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'quantity', 'description']

    def clean_quantity(self):
        quan = self.cleaned_data['quantity']
        if quan <= 0:
            raise forms.ValidationError("Add quantity")
        return quan
