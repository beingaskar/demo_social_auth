"""demo_social_auth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from django.contrib.auth import views as auth_views

from core import views as core_views

urlpatterns = [

    # Adminpanel URL's
    path('admin/', admin.site.urls),

    # `python-social-auth` url's
    path('social-auth/', include('social_django.urls', namespace="social")),

    path('login', core_views.UserLogin.as_view(), name="login"),
    path('', core_views.Home.as_view(), name="home"),
    path('logout', auth_views.LogoutView.as_view(), name="logout"),

]
