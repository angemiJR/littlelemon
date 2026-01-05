from django.contrib import admin 
from django.urls import path 
from .views import MenuItemView, SingleMenuItemView
from . import views
#from rest_framework.authtoken.views import obtain_auth_token

app_name = "restaurant"
  
urlpatterns = [
    path('', views.home, name='home'),
    #path('menu/', MenuItemView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', SingleMenuItemView.as_view(), name='single-menu-item'),
    #path("message/", views.msg),
    #path("api-token-auth/", obtain_auth_token),
    
    path("about/", views.about, name='about'),
    path("menu/", views.menu, name="menu"),
    path("book/", views.booking_page, name="book"), 
]