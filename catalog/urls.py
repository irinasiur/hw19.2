from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from django.urls import path

from catalog import views
from catalog.apps import CatalogConfig
from catalog.views import contacts, ProductListView, ProductDetailView, CategoriesListView, CategoriesDetailView, \
    ProductCreateView, ProductUpdateView, ProductDeleteView, VersionListView, VersionCreateView, VersionUpdateView, \
    VersionDeleteView, VersionDetailView
from config import settings


app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name="index"),
    path('create/', ProductCreateView.as_view(), name="create_product"),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='view_product'),
    path('contacts/', views.contacts, name='contacts'),
    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('product/<int:pk>/', CategoriesDetailView.as_view(), name='product'),
    path('accounts/login/', LoginView.as_view(), name='login'),

    path('', VersionListView.as_view(), name="index"),
    path('create/', VersionCreateView.as_view(), name="create_version"),
    path('update/<int:pk>/', VersionUpdateView.as_view(), name='update_version'),
    path('delete/<int:pk>/', VersionDeleteView.as_view(), name='delete_version'),
    path('product/<int:pk>/', VersionDetailView.as_view(), name='view_version'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)