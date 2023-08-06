from django.urls import path

from catalog import views
from catalog.views import index, contacts

urlpatterns = [
    path('', views.index, name="index"),
    path('contacts/', views.contacts, name='contacts'),
]