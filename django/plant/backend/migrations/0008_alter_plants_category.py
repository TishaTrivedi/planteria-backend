# Generated by Django 4.2.3 on 2023-07-24 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0007_remove_plants_shortdesc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plants',
            name='category',
            field=models.CharField(choices=[('zodiac', 'Zodiac'), ('flowering', 'Flowering'), ('low_maintain', 'Low_Maintenance'), ('medicinal', 'Medicinal'), ('air_purifying', 'Air_Purifying'), ('pet-friendly', 'Pet-Friendly')], max_length=50),
        ),
    ]
