"""first_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views     # Just importing views.py

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', views.user_list),
    path('users/<int:pk>/', views.user_detail),
    path('index/', views.index, name='index'),   # URL of the index of website.
    path('',views.index,name='index'),
    path('classes/', views.classes, name='classes'),
    path('navbar/', views.navbar, name='navbar'),
    path('notes/',views.notes, name='notes'),
    path('books/',views.books, name='books'),
    path('player/',views.player, name='player')
]
