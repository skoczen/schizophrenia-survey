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
    user = models.ForeignKey('auth.User', editable=False)
    entrance_id = models.CharField(max_length=255)
    exit_url = models.TextField(max_length=255)
    start_time = models.DateTimeField(auto_now_add=True)
    finish_time = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return "User %s" % self.entrance_id

    @property
    def ratings(self):
        return self.healthstaterating_set.all()

    def _completed_state(self, order):
        try:
            return self.ratings.get(order=order).finished()
        except HealthStateRating.DoesNotExist:
            return False

    def completed_state_1(self):
        return self._completed_state(1)

    def completed_state_2(self):
        return self._completed_state(2)

    def completed_state_3(self):
        return self._completed_state(3)

    def completed_state_4(self):
        return self._completed_state(4)

    def completed_state_5(self):
        return self._completed_state(5)

    def completed_state_6(self):
        return self._completed_state(6)

    def completed_state_7(self):
        return self._completed_state(7)

    def completed_state_8(self):
        return self._completed_state(8)

    completed_state_1.boolean = True
    completed_state_1.short_description = "1"
    completed_state_2.boolean = True
    completed_state_2.short_description = "2"
    completed_state_3.boolean = True
    completed_state_3.short_description = "3"
    completed_state_4.boolean = True
    completed_state_4.short_description = "4"
    completed_state_5.boolean = True
    completed_state_5.short_description = "5"
    completed_state_6.boolean = True
    completed_state_6.short_description = "6"
    completed_state_7.boolean = True
    completed_state_7.short_description = "7"
    completed_state_8.boolean = True
    completed_state_8.short_description = "8"

    def started(self):
        return self.start_time is not None

    def finished(self):
        return self.finish_time is not None

    started.boolean = True
    finished.boolean = True


class HealthStateRating(models.Model):
    order = models.IntegerField()
    survey_response = models.ForeignKey(SurveyResponse)
    health_state = models.ForeignKey(HealthState)
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

    def started(self):
        return self.start_time is not None

    def finished(self):
        return self.finish_time is not None

    started.boolean = True
    finished.boolean = True

# Patch to prevent superuser delete
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

@receiver(pre_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    if instance.is_superuser:
        raise PermissionDenied