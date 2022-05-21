from django.contrib import admin
from Tienda.models import *
# Register your models here.
class CategoriaProdAdmin(admin.ModelAdmin):
    list_display=("nombre",)


class ProductoAdmin(admin.ModelAdmin):
    #readonly_fields=("created","updated")
    list_display=("titulo",'precio',)


admin.site.register(CategoriaProd,CategoriaProdAdmin)
admin.site.register(Producto,ProductoAdmin)