from django.conf.urls.static import static
from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, CategoriesListView, CategoriesDetailView
from config import settings

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="index"),
    path('contacts/', views.contacts, name='contacts'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('product/<int:pk>/', CategoriesDetailView.as_view(), name='product'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)