# Generated by Django 5.0.6 on 2025-02-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Locations_map', '0008_remove_locations_map_location_store_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='locations_map',
            name='store_img',
            field=models.ImageField(null=True, upload_to='Locations-map'),
        ),
    ]
