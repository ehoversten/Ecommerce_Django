from django import forms
from ..product.models import productModels, detailsModels

class productForm(forms.ModelForm):
    class Meta:
        model = productModels.Product
        fields = [
            'name',
            'brand',
            'description',
            'price',
        ]

    class colorForm(forms.ModelForm):
        class Meta:
            model = detailsModels.Color
            fields = [
                'name',
            ]
            
    class sizeForm(forms.ModelForm):
        class Meta:
            model = detailsModels.Color
            fields = [
                'name',
            ]
    class categoryForm(forms.ModelForm):
        class Meta:
            model = detailsModels.Color
            fields = [
                'name',
            ]

