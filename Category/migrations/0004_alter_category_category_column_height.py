# Generated by Django 5.0.6 on 2025-02-17 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0003_alter_category_category_column_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_column_height',
            field=models.CharField(max_length=3),
        ),
    ]
