# Generated by Django 4.2.3 on 2023-09-03 10:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0014_alter_plants_images'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plants',
            name='images',
        ),
    ]