from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from pages.views import category, contacts, index, katalog, product

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('katalog/', katalog, name='katalog'),
    path('category/<slug:slug>/', category, name='category'),
    path('product/<int:product_id>/',product, name='product')
]

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   