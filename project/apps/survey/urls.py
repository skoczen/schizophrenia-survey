from django.conf.urls.defaults import patterns, include, url

from .views import survey_views, admin_views

urlpatterns = patterns('',
    url(r'^temp-logout$', survey_views.temp_logout, name='temp_logout'),

    url(r'^$', survey_views.entrance, name='entrance'),
    url(r'^next-page$', survey_views.next_page, name='next_page'),
    url(r'^survey$', survey_views.in_survey, name='in_survey'),
    url(r'^basic-info$', survey_views.demographics, name='demographics'),
    url(r'^complete$', survey_views.complete, name='complete'),
    url(r'^Unknown-Code$', survey_views.unknown_code, name='unknown_code'),

    url(r'^administration/dashboard/?$', admin_views.dashboard, name='admin_dashboard'),
    url(r'^administration/export/?$', admin_views.data_export, name='admin_data_export'),
    url(r'^administration/export/generate/?$', admin_views.generate_new_export, name='admin_generate_new_export'),
    url(r'^administration/upload-sequence/?$', admin_views.upload_sequence, name='upload_sequence'),
)
