from django.db import models
from Store.models import Store

# Create your models here.


class product_variations(models.Model):
    size = models.CharField(max_length=20, blank=True)
    color = models.CharField(max_length=20, blank=True)
    feature= models.TextField(max_length=60, blank=True)
    material_care = models.TextField(max_length=100, blank=True)
    product = models.ForeignKey(Store, on_delete=models.CASCADE)



    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Product Variations'