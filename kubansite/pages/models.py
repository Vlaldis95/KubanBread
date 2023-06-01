from django.db import models
from django.urls import reverse


class Packaging(models.Model):
    name = models.CharField(max_length=50, verbose_name='Название упаковки')
    photo = models.ImageField(
        verbose_name='Изображение',
        blank=True,
        upload_to='packages')
    description = models.TextField(
        verbose_name='Описание', max_length=200, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Упаковка'
        verbose_name_plural = 'Виды упаковки'


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
    packages = models.ManyToManyField(
        Packaging, related_name="products_packages", verbose_name='упаковка',
        max_length=10)
    pub_date = models.DateTimeField('Дата загрузки', auto_now=True)
    photo = models.ImageField(
        verbose_name='Изображение',
        blank=True,
        upload_to='pages')
    weight = models.CharField(verbose_name='Вес', max_length=10)
    title = models.CharField(verbose_name='Название', max_length=100)
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
