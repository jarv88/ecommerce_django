from django.conf import settings
from django.db import models

# Create your models here.

#Para que la carpeta de guardado de cada imagen sea independiente
def product_directory_path(instance,filename):
    return 'products/{0}/{1}'.format(instance.title, filename)


class CategoryProd(models.Model):
    name= models.CharField(max_length=20)

    class Meta:
        verbose_name="CategoryProd"
        verbose_name_plural="CategoriesProd"
    def __str__(self):
        return self.name

class Product(models.Model):
    code = models.CharField(max_length=50)
    title= models.CharField(max_length=50)
    image = models.ImageField(upload_to=product_directory_path, null=True, blank=True)
    description=models.CharField(max_length=150)
    price = models.FloatField()
    categories=models.ManyToManyField("CategoryProd")

    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"
    def __str__(self):
        return f"{self.code}-{self.title}"

class Sale(models.Model):
    idSale= models.AutoField(primary_key=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.SET_NULL,null=True,verbose_name="User")
    shippingAddress = models.TextField("Shipping address", blank=True)
    billingAddress = models.TextField("Billing address", blank=True)
    ref = models.CharField("Reference",max_length=128,help_text="A order reference.")
    subtotal = models.DecimalField("Subtotal", max_digits=18, decimal_places=2, default=0)
    total = models.DecimalField("Total", max_digits=18, decimal_places=2, default=0)
    date_created = models.DateTimeField("Date created", auto_now_add=True)
    date_updated = models.DateTimeField("Date updated", auto_now=True)

    class Meta:
        verbose_name="Sale"
        verbose_name_plural="Sales"
    def __str__(self):
        return f"{self.idSale} - {self.user.username} ({self.total})"


class SaleItem(models.Model):
    idSale= models.ForeignKey(Sale, on_delete=models.CASCADE)#models.IntegerField()
    codeProduct=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField(default=0.00)
    price=models.FloatField(default=0.00)
    total=models.FloatField(default=0.00) #price x quantity
    date_created = models.DateTimeField("Date created", auto_now_add=True)
    date_updated = models.DateTimeField("Date updated", auto_now=True)

    class Meta:
        verbose_name="SaleItem"
        verbose_name_plural="SaleItems"
    def __str__(self):
        return f"{self.idSale} - {self.codeProduct} ({self.total})"


