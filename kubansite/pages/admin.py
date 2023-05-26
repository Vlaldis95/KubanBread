from django.contrib import admin
from .models import Category, Product


class ProductAdmin(admin.ModelAdmin):
    fields = ('title', 'category', 'photo', 'packaging',
              'weight', 'expiration_date', 'quantity_a')
    list_display = ('title', 'category', 'photo', 'pub_date',
                    'packaging', 'weight', 'expiration_date', 'quantity_a')
    search_fields = ('title',)
    list_filter = ('pub_date',)


class CategoryAdmin(admin.ModelAdmin):
    fields = ('title', 'slug')
    search_fields = ('title',)
    list_display = ('id', 'title')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
