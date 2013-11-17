from django.contrib import admin
from models import HealthState, SurveyPath, SurveyResponse, HealthStateRating

class SurveyResponseOptions(admin.ModelAdmin):
    list_display = ('entrance_id',
                    'start_time',
                    'started',
                    'completed_state_1',
                    'completed_state_2',
                    'completed_state_3',
                    'completed_state_4',
                    'completed_state_5',
                    'completed_state_6',
                    'completed_state_7',
                    'completed_state_8',
                    'finished', )
    search_fields = ('entrance_id', 'user__email')

admin.site.register(HealthState)
admin.site.register(SurveyPath)
admin.site.register(SurveyResponse, SurveyResponseOptions)
# admin.site.register(HealthStateRating)
