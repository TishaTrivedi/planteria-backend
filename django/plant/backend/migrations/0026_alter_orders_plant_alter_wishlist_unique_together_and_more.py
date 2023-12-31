# Generated by Django 4.2.3 on 2023-09-16 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0025_alter_wishlist_unique_together_remove_orders_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='plant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.plants'),
        ),
        migrations.AlterUniqueTogether(
            name='wishlist',
            unique_together={('customerId', 'plantId')},
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='productId',
        ),
    ]
