"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from airlines.views import  airline_home_page
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views
#from project1.views import AccountLoginView, AccountLogoutConfirmationView, AccountLogoutYesNoView, AccountLogoutView

urlpatterns = [
    path("", airline_home_page, name="home"),
    path("admin/", admin.site.urls),
    path("airlines/", include("airlines.urls")),
    # LOGIN LOGOUT
    #path('login-confirmation/', AccountLoginConfirmationView.as_view(), name='login-confirmation'),
    #path('logout-confirmation/', AccountLogoutConfirmationView.as_view(), name='logout-confirmation'),
    #path('logout-yes-no-confirmation/', AccountLogoutYesNoView.as_view(), name='logout-yes-no-confirmation'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
]
