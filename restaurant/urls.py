from django.contrib import admin 
from django.urls import path 
from .views import MenuItemView, SingleMenuItemView
from . import views
from rest_framework.authtoken.views import obtain_auth_token
  
urlpatterns = [
    path('menu/', MenuItemView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='single-menu-item'),
    path("message/", views.msg),
    path("api-token-auth/", obtain_auth_token),
]