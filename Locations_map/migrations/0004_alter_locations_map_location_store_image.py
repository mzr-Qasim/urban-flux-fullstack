# Generated by Django 5.0.6 on 2025-02-26 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Locations_map', '0003_alter_locations_map_location_svg_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='locations_map',
            name='location_store_image',
            field=models.ImageField(null=True, upload_to='Locatoins-map'),
        ),
    ]
