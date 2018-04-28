from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^leaflet/$', views.leaflet, name='leaflet'),
    url(r'^analysis/$', views.analysis, name='analysis'),
]
