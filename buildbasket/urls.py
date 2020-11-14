from django.contrib import admin
from django.urls import path
from . import views
# from .forms import BasketForm1, BasketForm2, BasketForm3

urlpatterns = [
    path('', views.step1, name='step1'),
    path('step2/', views.step2, name='step2'),
    path('step3/', views.step3, name='step3'),
    path('done/', views.done, name='done'),
]
