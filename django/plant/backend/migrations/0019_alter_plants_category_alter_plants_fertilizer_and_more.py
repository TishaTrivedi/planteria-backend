# Generated by Django 4.2.3 on 2023-09-07 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0018_rename_likeplants_wishlist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plants',
            name='category',
            field=models.CharField(choices=[('zodiac', 'Zodiac'), ('flowering', 'Flowering'), ('low_maintain', 'Low_Maintenance'), ('medicinal', 'Medicinal'), ('air_purifying', 'Air_Purifying'), ('pet-friendly', 'Pet-Friendly')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='plants',
            name='fertilizer',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='plants',
            name='subcategory',
            field=models.CharField(choices=[('indoor', 'Indoor'), ('outdoor', 'Outdoor')], default='Indoor', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='plants',
            name='sunlight',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='plants',
            name='water',
            field=models.CharField(max_length=1000, null=True),
        ),
    ]
