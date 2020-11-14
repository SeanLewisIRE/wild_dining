from django import forms
from .models import buildBasket

class CheeseForm(forms.ModelForm):
    cheesesSelection1 = forms.CheckboxInput()
    cheesesSelection2 = forms.CheckboxInput()
    
    class Meta:
        model = buildBasket
        fields = ('id',)
