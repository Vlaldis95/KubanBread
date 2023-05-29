import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import admin, auth

from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'photo', 'packaging',
              'weight', 'expiration_date', 'quantity_a')
    list_display = ('title', 'category', 'photo', 'pub_date',
                    'packaging', 'weight', 'expiration_date', 'quantity_a')
    search_fields = ('title',)
    list_filter = ('pub_date', 'title')


class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'slug')
    search_fields = ('title',)
    list_display = ('id', 'title')
    list_filter = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
