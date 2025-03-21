# Generated by Django 5.0.6 on 2025-02-22 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0011_remove_category_cat_half_col_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.CharField(blank=True, choices=[('CASUAL', 'Casual'), ('LUXURY', 'Luxury')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='type_button',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='type_description',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
