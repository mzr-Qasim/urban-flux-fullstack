# Generated by Django 5.0.6 on 2025-03-12 07:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0020_alter_store_sale'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='sale',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
