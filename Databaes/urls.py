"""Databaes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from account import views as custom_registration_views
from . import views

urlpatterns = [
    url(r'^$', views.homepage, name='homepage'),
    url(r'^admin/', admin.site.urls),
    url(r'^crate/', include('Crate.urls')),
    url(r'^login/', custom_registration_views.LoginView.as_view(), name='login'),
    url(r'^logout/', custom_registration_views.logoutView, name='logout'),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^register/', custom_registration_views.UserRegistrationFormView.as_view(), name='register'),
]
