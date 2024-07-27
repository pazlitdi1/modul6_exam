from django import forms
from shop.models import Shop


class ProductForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ('title', 'slug', 'description', 'price', 'categories')
