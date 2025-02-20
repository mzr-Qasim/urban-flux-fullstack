from django.db import models

# Create your models here.
class Cloth_Class(models.Model):
    cloth_class_name = models.CharField(max_length=100)
    cloth_class_info = models.CharField(max_length=100)
    cloth_class_link_name = models.CharField(max_length=20)
    image = models.ImageField(upload_to= 'Categories/Cloth_Class')


    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Cloth Class'
