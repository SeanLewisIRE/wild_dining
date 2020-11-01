from django import forms
from products.models import Product


# class BasketForm1(forms.Form):
#     products = forms.SelectMultipleField(
#         queryset=Product.objects.filter(id=1),
#         widget=forms.CheckboxSelectMultiple,
#     )

# class BasketForm2(forms.Form):
#     products = forms.ModelMultipleChoiceField(
#         queryset=Product.objects.filter(id=1),
#         widget=forms.CheckboxSelectMultiple,
#     )

# class BasketForm3(forms.Form):
#     products = forms.ModelMultipleChoiceField(
#         queryset=Product.objects.filter(id=1),
#         widget=forms.CheckboxSelectMultiple,
#     )
