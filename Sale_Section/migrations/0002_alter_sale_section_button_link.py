# Generated by Django 5.0.6 on 2025-02-18 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sale_Section', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale_section',
            name='button_link',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
