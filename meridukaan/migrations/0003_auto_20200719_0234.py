# Generated by Django 3.0.8 on 2020-07-18 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meridukaan', '0002_auto_20200716_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='static/images/no-image.jpeg', upload_to='static/p-image'),
        ),
    ]
