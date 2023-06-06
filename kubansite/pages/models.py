from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название категории')
    slug = models.SlugField(
        unique=True,
        help_text='Ввести краткое название на латиннице, которое будет добавляться к основному url для адреса категории')
    photo = models.ImageField(
        verbose_name='Изображение',
        blank=True,
        upload_to='category_images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Категория продукции'
        verbose_name_plural = 'Категории продукции'


class Product(models.Model):
    pub_date = models.DateTimeField('Дата загрузки', auto_now=True)
    photo = models.ImageField(
        verbose_name='Фото продукта',
        blank=True,
        upload_to='product_images')
    weight = models.CharField(verbose_name='Вес', max_length=10)
    title = models.CharField(verbose_name='Название', max_length=100)
    packaging = models.CharField(verbose_name='Виды упаковки', max_length=100,blank=True)
    expiration_date = models.CharField(
        verbose_name='Срок годности',
        max_length=15)
    quantity_a = models.CharField(
        verbose_name='Количество вложения',
        blank=True,
        null=True,
        max_length=15)
    category = models.ForeignKey(
        Category,
        blank=True,
        null=True, on_delete=models.CASCADE,
        related_name='products',
        verbose_name='Категория',)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery', verbose_name= 'Фото', blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    
    class Meta:
        verbose_name = 'Пункт'
        verbose_name_plural = 'Фото упаковки'
