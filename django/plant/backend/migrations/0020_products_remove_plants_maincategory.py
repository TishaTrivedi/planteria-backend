# Generated by Django 4.2.3 on 2023-09-07 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0019_alter_plants_category_alter_plants_fertilizer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mainCategory', models.CharField(choices=[('fertilizer', 'Fertilizers'), ('tool', 'Tools'), ('pot', 'Pots')], default='Fertilizers', max_length=100)),
                ('product_name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=1000)),
                ('price', models.IntegerField()),
                ('size', models.CharField(choices=[('large', 'Large'), ('medium', 'Medium'), ('small', 'Small')], max_length=50)),
                ('images', models.ImageField(blank=True, default='', null=True, upload_to='products/images')),
            ],
        ),
        migrations.RemoveField(
            model_name='plants',
            name='mainCategory',
        ),
    ]
