from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^equipo/(?P<equipo_id>[0-9]+)/$', views.teamdetail, name='teamdetail'),
    url(r'^partido/(?P<partido_id>[0-9]+)/$', views.matchdetail, name='matchdetail'),
]