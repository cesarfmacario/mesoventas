from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.mainpage),
        url(r'^login/$', views.login),
        url(r'^signup/$', views.signup),
        url(r'^logout/$', views.logout),
        #url(r'^producto/(?P<pk>[0-9]+)/$', views.mainpage),
        #url(r'^signup$', views.signup),
    ]