from django.db import models


class HealthState(models.Model):
    name = models.CharField(max_length=255)
    actor_is_male = models.BooleanField(default=False)
    is_a_side_effect = models.BooleanField(default=False)
    is_transitional = models.BooleanField(default=False)
    severity_rating = models.IntegerField(help_text="A number, higher is more severe. Used for logic checks.")

    video_url = models.CharField(max_length=255, blank=True, null=True)

    title = models.CharField(max_length=255, blank=True, null=True)
    intro_body = models.TextField(max_length=255, blank=True, null=True)
    vas_body = models.TextField(max_length=255, blank=True, null=True)
    tto_body = models.TextField(max_length=255, blank=True, null=True)
    outro_body = models.TextField(max_length=255, blank=True, null=True)


class SurveyPath(models.Model):
    state_1 = models.ForeignKey(HealthState, related_name='+')
    state_2 = models.ForeignKey(HealthState, related_name='+')
    state_3 = models.ForeignKey(HealthState, related_name='+')
    state_4 = models.ForeignKey(HealthState, related_name='+')
    state_5 = models.ForeignKey(HealthState, related_name='+')
    state_6 = models.ForeignKey(HealthState, related_name='+')
    state_7 = models.ForeignKey(HealthState, related_name='+')
    state_8 = models.ForeignKey(HealthState, related_name='+')


class SurveyResponse(models.Model):
    user = models.ForeignKey('auth.User')
    entrance_id = models.CharField(max_length=255)
    exit_url = models.TextField(max_length=255)
    start_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(blank=True, null=True)


class HealthStateRating(models.Model):
    survey_response = models.ForeignKey(SurveyResponse)
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)

    vas_rating = models.FloatField(blank=True, null=True)
    tto_rating = models.FloatField(blank=True, null=True)

    intro_started = models.BooleanField(default=False)
    intro_completed = models.BooleanField(default=False)
    intro_completed_time = models.DateTimeField(blank=True, null=True)

    vas_started = models.BooleanField(default=False)
    vas_completed = models.BooleanField(default=False)
    vas_completed_time = models.DateTimeField(blank=True, null=True)

    tto_started = models.BooleanField(default=False)
    tto_completed = models.BooleanField(default=False)
    tto_completed_time = models.DateTimeField(blank=True, null=True)

    outro_started = models.BooleanField(default=False)
    outro_completed = models.BooleanField(default=False)
    outro_completed_time = models.DateTimeField(blank=True, null=True)