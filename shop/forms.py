from django.forms import ModelForm
from .models import Item
from django import forms


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['title', 'price', 'category', 'image', 'discount_price', 'start_date', 'end_date']
        widgets = {'start_date': forms.DateTimeInput(attrs={'type': 'date'}),
                   'end_date': forms.DateTimeInput(attrs={'type': 'date'})}
