from django.db import models

# Create your models here.

class Categories(models.Model):
    category = models.CharField(max_length=30)

    class Meta:
        db_table = 'app_categories'

    def __str__(self):
        return self.category

class Product(models.Model):

    name = models.CharField(max_length=50, null=True)
    sku = models.CharField(max_length=254, null=True, blank=True)
    price = models.FloatField()
    info = models.TextField()
    image = models.ImageField()
    category = models.ForeignKey('Categories', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'app_product'

    def __str__(self):
        return self.name