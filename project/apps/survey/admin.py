from django.contrib import admin
from models import HealthState, SurveyPath, SurveyResponse, HealthStateRating, HealthStateSequenceUpload, ActionLog

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


class SurveyPathOptions(admin.ModelAdmin):
    list_display = ('order',
                    'used',
                    'state_1',
                    'state_2',
                    'state_3',
                    'state_4',
                    'state_5',
                    'state_6',
                    'state_7',
                    'state_8',
                    )


class HealthStateSequenceUploadOptions(admin.ModelAdmin):
    list_display = ('csv_file', 'uploaded_at',)


class ActionLogOptions(admin.ModelAdmin):
    list_display = ('user', 'action', 'when')


admin.site.register(HealthStateSequenceUpload, HealthStateSequenceUploadOptions)
admin.site.register(HealthState)
admin.site.register(SurveyPath, SurveyPathOptions)
admin.site.register(SurveyResponse, SurveyResponseOptions)
admin.site.register(ActionLog, ActionLogOptions)
# admin.site.register(HealthStateRating)
