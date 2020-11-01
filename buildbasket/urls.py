from django.contrib import admin
from django.urls import path
from . import views
# from .forms import BasketForm1, BasketForm2, BasketForm3

urlpatterns = [
    path('', views.step1, name='step1'),
    path('step2/', views.step2, name='step2'),
    path('last_step/', views.last_step, name='last_step'),
]
