from django.contrib import admin
from models import HealthState, SurveyPath, SurveyResponse, HealthStateRating

# class EmailSubscriptionOptions(admin.ModelAdmin):
#     list_display = ('email',)
#     search_fields = ('email',)

# admin.site.register(HealthState,EmailSubscriptionOptions)
admin.site.register(HealthState)
admin.site.register(SurveyPath)
admin.site.register(SurveyResponse)
admin.site.register(HealthStateRating)
