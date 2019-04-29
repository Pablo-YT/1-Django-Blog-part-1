"""blog URL Configuration

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
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import path
from django.contrib import admin
from blog.views import blog_page, title_view, root, home, login_view, logout_view, special, article_view




urlpatterns = [
    path('blog/', blog_page),
    path('admin/', admin.site.urls),
    path('title/<int:id>', title_view, name="title"),
    path('', root),
    path('home/', home, name='home_page'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('special/', special, name='special'),
    path('post/', article_view, name='post')
]

