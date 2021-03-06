"""dbms_proj URL Configuration

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
from timetable import views ## importing views from timetable app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register),
    path('create_user/', views.create_user),
    path('', views.index),
    path('welcomeadmin', views.welcomeadmin),
    path('welcometeach', views.welcometeach),
    path('welcomestudent', views.welcomestudent),
    path('dashboard/', views.dashboard),
    path('view/',views.view),
    path('freehour/',views.freehour),
    path('freehoursee/',views.freehoursee),
    path('createtable/',views.createtable),
    path('create_func/',views.create_func),
    path('interests/', views.interests),
    path('login_response/', views.login_response),
]
