from django import forms
from django.forms import ModelChoiceField
from products.models import Product


class BasketForm1(forms.Form):

    products = Product.objects.all().filter(category=1)
    CHOICES = []

    for product in products:
        print(product.pk, product.name)
        choice = {
            product.pk: product.name,
            product.name : product.name

        }
        CHOICES.append(choice)
    print(CHOICES)

    picked = forms.MultipleChoiceField(
        choices=(CHOICES), widget=forms.CheckboxSelectMultiple())


    # cheese1 = forms.ModelChoiceField(
    #     queryset=Product.objects.none())

    # def __init__(self, *args, **kwargs):
    #     super(BasketForm1, self).__init__(*args, **kwargs)
    #     self.fields['cheese1'].queryset = Product.objects.filter(category=1)

class BasketForm2(forms.Form):

    meat2 = forms.ModelChoiceField(
        queryset=Product.objects.none())

    def __init__(self, *args, **kwargs):
        super(BasketForm2, self).__init__(*args, **kwargs)
        self.fields['meat2'].queryset = Product.objects.filter(category=2)


class BasketForm3(forms.Form):

    drink1 = forms.ModelChoiceField(queryset=Product.objects.none())

    def __init__(self, *args, **kwargs):
        super(BasketForm3, self).__init__(*args, **kwargs)
        self.fields['drink1'].queryset = Product.objects.filter(category=4)
