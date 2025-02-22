from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

def validate_logo(value):
    # Check the file extension
    valid_extensions = ['.svg', '.png', '.jpg', '.jpeg', '.gif']
    if not any(value.name.endswith(ext) for ext in valid_extensions):
        raise ValidationError('File must be an SVG or an image file.')


class Site_Settings(models.Model):
    estimated_delivery = models.TextField(max_length= 200, null=True)
    return_time = models.TextField(max_length= 200 , null=True)
    site_logo = models.FileField(upload_to='site_logo', validators=[validate_logo])
    theme_hero_section = models.ImageField(upload_to= 'theme_hero_section')
    tax_rate = models.IntegerField()
    product_policies = models.TextField(max_length=400)


    class Meta:
        verbose_name = ''
        verbose_name_plural = 'Site Settings'