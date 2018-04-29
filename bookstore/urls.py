from django.conf.urls import url
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.home),
    url(r'^login$', views.login, name='himanshu'),
    url(r'^register', views.register, name='shubham'),
    url(r'^homepage$', views.home, name='hemu'),
    url(r'^dota$', views.dota, name='dotame'),
    url(r'^copyright$', views.copyright, name='copy'),
    url(r'^donate$', views.donate, name='donate'),
    url(r'^shortstory$', views.shortstory, name='shortstory'),
    url(r'^novels$', views.novels, name='novels'),
    url(r'^art$', views.art, name='art'),
    url(r'^creative$', views.creative, name='creative'),
    url(r'^novels1$', views.novels1, name='novels1'),
    url(r'^art1$', views.art1, name='art1'),
    url(r'^creative1$', views.creative1, name='creative1'),
    url(r'^take$', views.take, name='take'),
    url(r'^contact$', views.contact, name='contact'),
    url(r'^add$', views.add, name='add'),
    url(r'^view$', views.view, name='view'),
    url(r'^logout$', auth_views.logout, {'template_name': 'bookstore/logout.html'}, name='logout'),

]
