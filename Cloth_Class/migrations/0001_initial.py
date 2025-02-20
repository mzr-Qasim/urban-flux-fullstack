# Generated by Django 5.0.6 on 2025-02-20 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cloth_Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cloth_class_name', models.CharField(max_length=100)),
                ('cloth_class_info', models.CharField(max_length=100)),
                ('cloth_class_link_name', models.CharField(max_length=20)),
                ('image', models.ImageField(upload_to='Categories/Cloth_Class')),
            ],
            options={
                'verbose_name': '',
                'verbose_name_plural': 'Cloth Class',
            },
        ),
    ]
