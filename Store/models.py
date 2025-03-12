from django.db import models
from django.urls import reverse
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
from Category.models import Category

class Store(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(null=True)
    product_type = models.CharField(max_length=15, blank=True)
    description = models.TextField(max_length=500)
    stock = models.IntegerField()
    sale = models.IntegerField(null=True,
        validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    is_available = models.BooleanField(default = True)
    slug =models.SlugField(max_length=100, unique=True)
    image = models.ImageField(upload_to='Products')
    product_image_1 = models.ImageField(upload_to='Products')
    product_image_2 = models.ImageField(upload_to='Products')
    product_image_3 = models.ImageField(upload_to='Products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)




    def get_url(self):
        return reverse('products_detail', args=(self.category.slug))

    class Meta():
        verbose_name = ''
        verbose_name_plural = 'Product'
    


    def __str__(self):
        return self.name 


