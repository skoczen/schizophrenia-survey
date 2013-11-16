from django.conf.urls.defaults import patterns, include, url

from survey import views

urlpatterns = patterns('',
    url(r'^$', views.entrance, name='entrance'),
    url(r'^next-page$', views.next_page, name='next_page'),
    url(r'^in-survey$', views.in_survey_stub, name='in_survey_stub'),
    url(r'^Unknown-Code$', views.unknown_code, name='unknown_code'),
)
