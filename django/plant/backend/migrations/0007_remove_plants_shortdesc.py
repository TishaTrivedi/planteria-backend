# Generated by Django 4.2.3 on 2023-07-24 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0006_alter_plants_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plants',
            name='shortdesc',
        ),
    ]