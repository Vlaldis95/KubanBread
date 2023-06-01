import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import admin, auth

from .models import Category, Packaging, Product


class PackagingAdmin(admin.ModelAdmin):
    list_display = ('name', 'photo', 'description')
    list_per_page = 10
    search_fields = ('name',)
    list_filter = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title', 'category', 'photo',
        'weight', 'quantity_a', 'expiration_date')
    list_per_page = 10
    search_fields = ('title',)
    list_filter = ('pub_date', 'title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'photo')
    search_fields = ('title',)
    list_per_page = 10
    list_filter = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Packaging, PackagingAdmin)
admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
