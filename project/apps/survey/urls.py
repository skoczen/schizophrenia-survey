from django.conf.urls.defaults import patterns, include, url

from survey import views

urlpatterns = patterns('',
    url(r'^$', views.entrance, name='entrance'),
    url(r'^next-page$', views.next_page, name='next_page'),
    url(r'^in-survey$', views.in_survey_stub, name='in_survey_stub'),
    url(r'^complete$', views.complete, name='complete'),
    url(r'^Unknown-Code$', views.unknown_code, name='unknown_code'),

    url(r'^administration/upload-sequence[/]?$', views.upload_sequence, name='upload_sequence'),
)
