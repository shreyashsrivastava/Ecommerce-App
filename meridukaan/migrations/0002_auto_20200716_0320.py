# Generated by Django 3.0.8 on 2020-07-15 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meridukaan', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_id',
        ),
        migrations.AddField(
            model_name='product',
            name='product_image',
            field=models.ImageField(default='static/images/no-image.jpeg', upload_to=''),
        ),
    ]
