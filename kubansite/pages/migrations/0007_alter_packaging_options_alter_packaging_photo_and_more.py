# Generated by Django 4.2.1 on 2023-06-01 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_packaging_remove_product_packaging_product_packages'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='packaging',
            options={'verbose_name': 'Упаковка', 'verbose_name_plural': 'Виды упаковки'},
        ),
        migrations.AlterField(
            model_name='packaging',
            name='photo',
            field=models.ImageField(blank=True, upload_to='packages', verbose_name='Изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='packages',
            field=models.ManyToManyField(max_length=10, related_name='products_packages', to='pages.packaging', verbose_name='упаковка'),
        ),
    ]
