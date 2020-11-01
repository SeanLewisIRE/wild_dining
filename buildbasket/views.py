from django.shortcuts import render, redirect
from products.models import Product
from .forms import BasketForm1, BasketForm2, BasketForm3
from formtools.wizard.views import SessionWizardView
from bag.views import add_to_bag
# Create your views here.

class BasketWizard(SessionWizardView):

    template_name = "buildbasket/wizard_form.html"
    form_list = [BasketForm1, BasketForm2, BasketForm3]

    

    def done(self, form_list, **kwargs):

        for item in form_list:
            print(item)
        
        return redirect('../bag/bag.html')

        # return render(self.request, 'bag/bag.html',  {
        #     'form_data': [form.cleaned_data for form in form_list],
        # })
