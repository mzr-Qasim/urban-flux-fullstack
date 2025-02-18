from django.db import models

# Create your models here.
from Category.models import Category

class Store(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_type = models.CharField(max_length=15)
    description = models.TextField(max_length=500, blank=True)
    Color = models.CharField(max_length=10)
    Feature = models.CharField(max_length=50)
    Size = models.CharField(max_length=50)
    stock = models.IntegerField()
    sale = models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField(default = True)
    slug =models.SlugField(max_length=100, unique=True)
    Image = models.ImageField(upload_to='Categories')
    product_image_1 = models.ImageField(upload_to='Categories')
    product_image_2 = models.ImageField(upload_to='Categories')
    product_image_3 = models.ImageField(upload_to='Categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


    class Meta():
        verbose_name = ''
        verbose_name_plural = 'Product'


