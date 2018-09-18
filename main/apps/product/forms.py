from django import forms
from .models import Product
# CATAGORY = [(Category.name, Category.name.val)]


# class createProduct(forms.Form):
#     name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Product Name"}))

#     brand = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Product Brand"}))

#     description = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": " Please provide a description."}))

#     price = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}))

#     quantity = forms.CharField(widget=forms.NumberInput(attrs={"class": "form-control"}))

#     # seller = forms.CharField(widget=forms.MultipleChoiceField(attrs={"class": "form-control"}))

#     thumb = forms.FileField()

#     instock = forms.CharField(widget=forms.CheckboxInput(attrs={"class": "form-check-input"}))

#     active = forms.CharField(widget=forms.CheckboxInput(attrs={"class": "form-check-input check-box"}))

#     # choices = forms.CharField(widget=forms.Select(choices=Category))


# class createCategoryForm(forms.Form):
#     cName = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Category Name"}))

""" class productForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'brand',
            'description',
            'price',
        ]

 """
