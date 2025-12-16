from django.contrib import admin 
from django.urls import path 
from .views import MenuItemView, SingleMenuItemView
from . import views
  
urlpatterns = [
    path('menu/', MenuItemView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='single-menu-item'),
]