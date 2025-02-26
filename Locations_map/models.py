from django.db import models

# Create your models here.


class Locations_map(models.Model):
    location_title = models.CharField(max_length=10)
    location_map_image = models.ImageField(upload_to= "Locations-map")
    location_svg_code = models.TextField(max_length=2000)



    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Locations Map'