from django import forms

from products.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price","quantity","minQuantity","type","image"]


class ProductUpdateForm(forms.Form):
    name=forms.CharField(max_length=200,required=False)
    price=forms.FloatField(required=False)
    quantity=forms.IntegerField(required=False)
    minQuantity=forms.IntegerField(required=False)
    type=forms.CharField(max_length=200,required=False)
    image=forms.ImageField(allow_empty_file=True,required=False)