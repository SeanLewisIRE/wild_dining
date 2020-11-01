from django import forms
from django.forms import ModelChoiceField
from products.models import Product


class BasketForm1(forms.Form):

    cheese_selection1 = forms.ModelChoiceField(
        queryset=Product.objects.filter(category=1))
    cheese_selection2 = forms.ModelChoiceField(
        queryset=Product.objects.filter(category=1))


class BasketForm2(forms.Form):
    meat_selection1 = forms.ModelChoiceField(
        queryset=Product.objects.filter(category=2))
    meat_selection2 = forms.ModelChoiceField(
        queryset=Product.objects.filter(category=2))


class BasketForm3(forms.Form):
    drink_selection1 = forms.ModelChoiceField(
        queryset=Product.objects.filter(category=4))
