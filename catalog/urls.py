from django.conf.urls.static import static
from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import index, contacts
from config import settings

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.index, name="index"),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:product_id>/', views.product, name='product'),
    path('categories/', views.categories, name='categories'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)