from django.db import models

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    cat_image = models.ImageField(upload_to= 'Categories', null=True, blank=True)
    cat_half_col_name = models.CharField(max_length=255, unique=True, null=True, blank=True)
    cat_image_half_col = models.ImageField(upload_to= 'Categories', null=True, blank=True)
    slug =models.SlugField(max_length=100, unique=True)
    category_col_height = models.CharField(max_length=4, null=True)


    class Meta:
        verbose_name= ''
        verbose_name_plural = 'Categories'




    def __str__(self):
        return self.category_name