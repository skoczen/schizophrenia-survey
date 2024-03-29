from django.conf.urls.defaults import patterns, include, url

from .views import survey_views, admin_views

urlpatterns = patterns('',
    url(r'^tinymce/', include('tinymce.urls')),

    url(r'^temp-logout$', survey_views.temp_logout, name='temp_logout'),

    url(r'^next-screen/(?P<last_screen_id>\d+)/$', survey_views.next_screen, name='next_screen'),
    url(r'^current-screen/$', survey_views.go_to_current, name='go_to_current'),
    url(r'^screen/$', survey_views.specific_screen, name='specific_screen'),

    url(r'^$', survey_views.entrance, name='entrance'),
    url(r'^basic-info/$', survey_views.demographics, name='demographics'),
    url(r'^about/$', survey_views.about, name='about'),
    url(r'^training/rating/$', survey_views.vas_training, name='vas_training'),
    url(r'^training/timeline/$', survey_views.tto_training, name='tto_training'),
    url(r'^introduction/$', survey_views.introduction, name='introduction'),
    url(r'^health-state/(?P<health_state_number>\d+)/intro/$', survey_views.health_state_intro, name='health_state_intro'),
    url(r'^health-state/(?P<health_state_number>\d+)/details/$', survey_views.health_state_video, name='health_state_video'),
    url(r'^health-state/(?P<health_state_number>\d+)/vas/$', survey_views.health_state_vas, name='health_state_vas'),
    url(r'^health-state/(?P<health_state_number>\d+)/tto/$', survey_views.health_state_tto, name='health_state_tto'),
    url(r'^health-state/(?P<health_state_number>\d+)/outro/$', survey_views.health_state_outro, name='health_state_outro'),
    url(r'^finished/$', survey_views.complete, name='complete'),

    url(r'^unknown-code/$', survey_views.unknown_code, name='unknown_code'),

    url(r'^administration/dashboard/?$', admin_views.dashboard, name='admin_dashboard'),
    url(r'^administration/export/$', admin_views.data_export, name='admin_data_export'),
    url(r'^administration/export/generate/$', admin_views.generate_new_export, name='admin_generate_new_export'),
    url(r'^administration/upload-sequence/$', admin_views.upload_sequence, name='upload_sequence'),
    url(r'^administration/survey-config/$', admin_views.survey_config, name='admin_survey_config'),
)
