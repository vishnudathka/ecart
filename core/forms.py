from django import forms
from core import models


class ProductForm(forms.ModelForm):
    images = forms.ImageField(required=False)

    class Meta:
        model = models.ProductModel
        fields = ["name", "discription", "price", "unit", "category"]
