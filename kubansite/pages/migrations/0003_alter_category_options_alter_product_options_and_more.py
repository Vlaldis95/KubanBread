# Generated by Django 4.2.1 on 2023-05-26 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_product_pub_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Категория продукции', 'verbose_name_plural': 'Категории продукции'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
        migrations.AlterField(
            model_name='category',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Название категории'),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='pages.category', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='product',
            name='packaging',
            field=models.CharField(blank=True, choices=[('Гофрокороб', 'Гофрокороб'), ('Телефизор', 'Телефизор')], max_length=10, verbose_name='Упаковка'),
        ),
    ]
