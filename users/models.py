from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class userProfiles(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15, null=True)
    last_name = models.CharField(max_length=15, null=True)
    country = models.CharField(max_length=30, null=True)
    street_address = models.TextField(max_length=255, null=True)
    optional_address = models.TextField(max_length=255, null=True)
    city = models.CharField(max_length=30, null=True)
    state = models.CharField(max_length=30, null=True)
    email = models.CharField(max_length=200, null=True)
    zip_code = models.CharField(null=True, max_length=10)
    phone = models.CharField(null=True, max_length=15)
    order_notes = models.TextField(null=True, max_length=255)


    class Meta:
        verbose_name = ''
        verbose_name_plural = 'User Profiles'