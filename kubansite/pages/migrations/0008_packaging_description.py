# Generated by Django 4.2.1 on 2023-06-01 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0007_alter_packaging_options_alter_packaging_photo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='packaging',
            name='description',
            field=models.TextField(blank=True, max_length=200, verbose_name='Описание'),
        ),
    ]