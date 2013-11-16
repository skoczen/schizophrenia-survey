from django.conf.urls.defaults import patterns, include, url

from survey import views

urlpatterns = patterns('',
    url(r'^$', views.entrance, name='entrance'),
    url(r'^Unknown-Code$', views.unknown_code, name='unknown_code'),
)
