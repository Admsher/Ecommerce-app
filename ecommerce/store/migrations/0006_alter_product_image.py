# Generated by Django 4.1.13 on 2024-07-17 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, default='static/images/placeholder.png', null=True, upload_to=''),
        ),
    ]
