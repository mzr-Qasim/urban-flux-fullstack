# Generated by Django 5.0.6 on 2025-02-22 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Site_Settings', '0002_alter_site_settings_site_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='site_settings',
            name='estimated_delivery',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='site_settings',
            name='return_time',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
