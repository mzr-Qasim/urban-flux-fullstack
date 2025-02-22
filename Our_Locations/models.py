from django.db import models

# Create your models here.

class Our_Locations(models.Model):
    location_city = models.CharField(max_length=20)
    location =  models.CharField(max_length= 100)
    email = models.CharField(max_length= 50)
    phone = models.CharField(max_length= 20)
    timings = models.CharField(max_length= 100)
    close_detail = models.CharField(max_length=50, null=True)
    Image = models.ImageField(upload_to= "Our_Locations")


    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Our Locations'