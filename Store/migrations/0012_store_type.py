# Generated by Django 5.0.6 on 2025-02-22 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0011_alter_store_product_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='type',
            field=models.CharField(choices=[('casual', 'Casual'), ('luxury', 'Luxury')], max_length=50, null=True),
        ),
    ]
