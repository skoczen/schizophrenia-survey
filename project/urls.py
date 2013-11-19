from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'', include('survey.urls', namespace="survey", app_name="survey")),
    url(r'administration/', include(admin.site.urls), name="admin"),


    url(r'^fonts/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': "%s/main_site/fonts" % settings.STATIC_ROOT,
    }),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
    }),
)
