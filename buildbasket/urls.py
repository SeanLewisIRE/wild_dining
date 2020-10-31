from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_cheese_products, name='buildBasket'),
]
