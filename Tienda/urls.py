from django.contrib import admin
from django.urls import path
from .views import *

app_name = 'Tienda'
urlpatterns = [
    path('', index, name="Index"),
    path('new_product/', newProduct, name="NewProduct"),
    path('new_category/', newCategory, name="NewCategory"),
]