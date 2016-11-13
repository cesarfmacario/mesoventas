from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.mainpage),
        url(r'^/login$', views.login),
    ]