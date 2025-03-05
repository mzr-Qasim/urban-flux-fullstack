from django.db import models
from django.urls import reverse

# Create your models here.
from Category.models import Category

class Store(models.Model):
    product_name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    product_type = models.CharField(max_length=15, blank=True)
    description = models.TextField(max_length=500)
    Color_1 = models.CharField(max_length=20 , null=True)
    Color_2 = models.CharField(max_length=20, null=True , blank=True)
    Color_3 = models.CharField(max_length=20, null=True , blank=True)
    Feature_1 = models.CharField(max_length=50, null=True)
    Feature_2 = models.CharField(max_length=50, null=True , blank=True)
    Feature_3 = models.CharField(max_length=50, null=True , blank=True)
    Size_1 = models.CharField(max_length=20 , null=True,)
    Size_2 = models.CharField(max_length=20, null=True , blank=True)
    Size_3 = models.CharField(max_length=20, null=True , blank=True)
    Materials_Care_1 = models.CharField(max_length=50, null=True)
    Materials_Care_2 = models.CharField(max_length=50, null=True , blank=True)
    Materials_Care_3 = models.CharField(max_length=50, null=True , blank=True)
    stock = models.IntegerField()
    sale = models.IntegerField(null=True, blank=True)
    is_available = models.BooleanField(default = True)
    slug =models.SlugField(max_length=100, unique=True)
    Image = models.ImageField(upload_to='Products')
    product_image_1 = models.ImageField(upload_to='Products')
    product_image_2 = models.ImageField(upload_to='Products')
    product_image_3 = models.ImageField(upload_to='Products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)




    def get_url(self):
        return reverse('products_detail', args=(self.category.slug))

    class Meta():
        verbose_name = ''
        verbose_name_plural = 'Product'


