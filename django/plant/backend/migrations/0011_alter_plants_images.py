# Generated by Django 4.2.3 on 2023-08-25 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0010_plants_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plants',
            name='images',
            field=models.ImageField(default='', upload_to='plant/images'),
        ),
    ]
