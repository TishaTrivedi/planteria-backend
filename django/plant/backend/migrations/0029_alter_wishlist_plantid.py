# Generated by Django 4.2.3 on 2023-09-16 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0028_remove_orders_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wishlist',
            name='plantId',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='backend.plants'),
        ),
    ]
