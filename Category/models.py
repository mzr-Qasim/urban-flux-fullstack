from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=255, unique=True)
    cat_image = models.ImageField(upload_to= 'Categories', null=True, blank=True)
    slug =models.SlugField(max_length=100, unique=True)
    TYPE_CHOICES = [
        ('FORMAL', 'Formal'),
        ('LUXURY', 'Luxury'),
    ]
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, null=True, blank=True)
    type_description = models.CharField(max_length=100, null=True, blank=True)
    type_button = models.CharField(max_length=20, null=True, blank=True)


    class Meta:
        verbose_name= ''
        verbose_name_plural = 'Categories'


    # def save(self, *args, **kwargs):
    #     # Automatically generate the slug from the name if not provided
    #     if not self.slug:
    #         self.slug = slugify(self.name)
    #     super().save(*args, **kwargs)


    def __str__(self):
        return self.category_name