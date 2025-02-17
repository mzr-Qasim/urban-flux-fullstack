from django.db import models

# Create your models here.
class Hero_Slider(models.Model):
    title = models.CharField(max_length=200)
    info = models.CharField(max_length=200)
    link_name = models.CharField(max_length=15)
    link = models.URLField(max_length=200, blank=True)
    image = models.ImageField(upload_to='hero_slider')

    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Hero Slider'

