import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import admin, auth

from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    list_display= ('title', 'category', 'photo', 'packaging',
              'weight', 'expiration_date', 'quantity_a')
    list_display_links = None
    list_per_page = 10
    list_editable = ('title','category', 'photo',
                    'packaging', 'weight', 'expiration_date', 'quantity_a')
    search_fields = ('title',)
    list_filter = ('pub_date', 'title')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug','photo')
    search_fields = ('title',)
    list_editable = ('title', 'slug','photo')
    list_display_links = None
    list_per_page = 10
    list_filter = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
