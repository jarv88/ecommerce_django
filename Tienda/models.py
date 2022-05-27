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
    title= models.CharField(max_length=50)
    image = models.ImageField(upload_to=product_directory_path, null=True, blank=True)
    description=models.CharField(max_length=150)
    price = models.FloatField()
    categories=models.ManyToManyField("CategoryProd")

    class Meta:
        verbose_name="Product"
        verbose_name_plural="Products"
    def __str__(self):
        return self.title

