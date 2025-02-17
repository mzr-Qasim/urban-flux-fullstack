# Generated by Django 5.0.6 on 2025-02-17 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=255, unique=True)),
                ('image', models.ImageField(upload_to='Categories')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('category_column_height', models.CharField(max_length=3)),
            ],
        ),
    ]
