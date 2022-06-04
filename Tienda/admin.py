from django.contrib import admin
from Tienda.models import *
# Register your models here.
class CategoryProdAdmin(admin.ModelAdmin):
    list_display=("name",)


class ProductAdmin(admin.ModelAdmin):
    #readonly_fields=("created","updated")
    list_display=("code","title",'price',)

class SaleAdmin(admin.ModelAdmin):
    #readonly_fields=("created","updated")
    list_display=('user',)

class SaleItemAdmin(admin.ModelAdmin):
    #readonly_fields=("created","updated")
    list_display=("idSale",'codeProduct','quantity','price','total')


admin.site.register(CategoryProd,CategoryProdAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Sale,SaleAdmin)
admin.site.register(SaleItem,SaleItemAdmin)
