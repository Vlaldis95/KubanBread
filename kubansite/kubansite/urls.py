from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from pages.views import category, contacts, index, katalog, product, privacy, agreement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('feedback/', contacts, name='contacts'),
    path('catalog/', katalog, name='katalog'),
    path('category/<slug:slug>/', category, name='category'),
    path('product/<int:product_id>/', product, name='product'),
    path('privacy/', privacy, name='privacy'),
    path('agreement/', agreement, name='agreement')
]
handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.e_handler500'
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
