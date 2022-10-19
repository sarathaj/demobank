"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path
from . import views
urlpatterns = [

      path('', views.index, name='index'),
      path('index', views.index, name='index'),

      path('new_page', views.new_page, name='new_page'),
      path('login', views.user_login_check, name='login'),
      path('user_logout', views.user_logout, name='user_logout'),
      path('register', views.register, name='register'),
      path('user_details_add', views.user_details_add, name='user_details_add'),



]
