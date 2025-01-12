# Generated by Django 4.2.1 on 2023-06-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_category_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packaging',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название упаковки')),
                ('photo', models.ImageField(blank=True, upload_to='package_images', verbose_name='Изображение')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='packaging',
        ),
        migrations.AddField(
            model_name='product',
            name='packages',
            field=models.ManyToManyField(max_length=10, to='pages.packaging', verbose_name='упаковка'),
        ),
    ]
