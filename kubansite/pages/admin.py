import django.contrib.auth.admin
import django.contrib.auth.models
from django.contrib import admin, auth

from .models import Category, Product, Gallery, WeightCategory

class WeightCategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_per_page = 10
    list_filter = ('title',)

class GalleryInline(admin.TabularInline):
    fk_name = 'product'
    model = Gallery


class ProductAdmin(admin.ModelAdmin):
    inlines = [GalleryInline,]
    list_display = (
        'title', 'category',
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
admin.site.register(WeightCategory, WeightCategoryAdmin)
admin.site.unregister(auth.models.User)
admin.site.unregister(auth.models.Group)
