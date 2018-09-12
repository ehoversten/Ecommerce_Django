from django import forms
from .models import Product
from .models import Color
from .models import Category


class createProduct(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ('created_at', 'updated_at', 'timestamp')


class createColor(forms.ModelForm):
    class Meta:
        model = Color
        exclude = ('created_at', 'updated_at', 'timestamp')
        
