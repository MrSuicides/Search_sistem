from .models import Product
from django.forms import ModelForm, TextInput, DateTimeInput


class FormProduct(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'statistical_weight', 'first_date', 'expiration_date']

        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название'
            }),
            "statistical_weight": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Склад'
            }),
            "first_date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата изготовления'
            }),
            "expiration_date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата окончания'
            })
        }
