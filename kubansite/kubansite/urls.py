from django.contrib import admin
from django.urls import path
from pages.views import index, contacts, katalog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('katalog/', katalog, name='katalog')
]
