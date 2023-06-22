"""lakspro URL Configuration

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

from laksapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.loginPage,name='login'),
    path('login',views.loginPage,name='login'),
    path('logout',views.loginPage,name='logout'),
    path('register',views.registerPage,name='register'),
    path('home',views.homePage,name='home'),
    path('contact',views.contactPage,name='contact'),
    path('service',views.servicePage,name='service'),
    path('feedback',views.feedbackPage,name='feedback'),
    path('gallery',views.galleryPage,name='gallery')
]