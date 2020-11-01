from django.contrib import admin
from django.urls import path
from .views import BasketWizard
from .forms import BasketForm1, BasketForm2, BasketForm3

urlpatterns = [
    path('', BasketWizard.as_view(
        [BasketForm1, BasketForm2, BasketForm3]), name='buildBasket'),
]
