from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.mainpage),
        url(r'^login/$', views.login),
        url(r'^signup/$', views.signup),
        url(r'^logout/$', views.logout),
        url(r'^productos/$', views.productos),
        url(r'^clientes/$', views.clientes),
        url(r'^productos/nuevo/$', views.producto_nuevo, name='producto_nuevo'),
        url(r'^clientes/nuevo/$', views.cliente_nuevo, name='cliente_nuevo'),
        url(r'^productos/editar/(?P<pk>[0-9]+)/$', views.producto_editar, name='producto_editar'),    
        url(r'^clientes/editar/(?P<pk>[0-9]+)/$', views.cliente_editar, name='cliente_editar'),
        #url(r'^producto/(?P<pk>[0-9]+)/$', views.mainpage),
        #url(r'^signup$', views.signup),
    ]