from django.db import models

# Create your models here.

class Sale_Section(models.Model):
    title = models.CharField(max_length = 50)
    heading = models.CharField(max_length = 50)
    description = models.TextField(max_length=100)
    link_button_name = models.CharField(max_length =15)
    button_link = models.CharField (max_length= 200, blank=True , null=True)
    image = models.ImageField(upload_to= 'Sale_Section')


    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Sale Section'