from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'Tienda'
urlpatterns = [
    path('', index, name="Index"),
    path('new_product/', newProduct, name="NewProduct"),
    path('new_category/', newCategory, name="NewCategory"),
    path('cart/', listCart, name="Cart"),
    path('cart/clean', cleanCart, name="CleanCart"),
    path('addCart/<int:idProduct>', addCart, name="AddCart"),
    path('cart/clean', cleanCart, name="CleanCart"),
]