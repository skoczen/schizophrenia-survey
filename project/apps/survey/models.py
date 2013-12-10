from django.db import models
from django.core.cache import cache
from .tasks import update_aggregate_tasks
from .screens import SCREENS

NEXT_SURVEY_PATH_KEY = "qi-next-survey-path-id"
EDUCATION_CHOICES = [
    ("Some high school", "Some high school"),
    ("High school diploma", "High school diploma"),
    ("Some college", "Some college"),
    ("College degree", "College degree"),
    ("Graduate degree", "Graduate degree"),
]
HOUSEHOLD_INCOME_CHOICES = [
    ("Less than 20,000", "Less than 20,000"),
    ("20,000-40,000", "20,000-40,000"),
    ("40,000-60,000", "40,000-60,000"),
    ("60,000-80,000", "60,000-80,000"),
    ("80,000-100,000", "80,000-100,000"),
    ("Greater than 100,000", "Greater than 100,000"),
]

class HealthStateSequenceUpload(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True, blank=True)
    csv_file = models.FileField(upload_to="sequences")


class HealthState(models.Model):
    number = models.IntegerField(unique=True)
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

    def __unicode__(self):
        return "Health State #%s" % self.number


class SurveyPath(models.Model):
    order = models.IntegerField(unique=True)
    used = models.BooleanField(default=False)
    state_1 = models.IntegerField()
    state_2 = models.IntegerField()
    state_3 = models.IntegerField()
    state_4 = models.IntegerField()
    state_5 = models.IntegerField()
    state_6 = models.IntegerField()
    state_7 = models.IntegerField()
    state_8 = models.IntegerField()

    class Meta:
        ordering = ("order",)

    @classmethod
    def get_next_path(cls):
        try:
            next_order = cache.incr(NEXT_SURVEY_PATH_KEY)
            next_path = cls.objects.get(order=next_order)
            next_path.save()
        except ValueError:
            # Cache key not set yet.
            if cls.objects.filter(used=False).count() > 0:
                next_path = cls.objects.filter(used=False).order_by("order")[0]
                next_order = next_path.order
                next_path.used = True
                next_path.save()
                cache.set(NEXT_SURVEY_PATH_KEY, next_order)

            else:
                from django.core.mail import mail_admins
                from traceback import format_exc
                mail_admins("CRITICAL: We're out of survey paths!",
                            "Survey.get_next_path() was just called, but there are no unused survey paths. \%s " % format_exc()
                            )
                return None

        return SurveyPath.objects.get(order=next_order)


class SurveyResponse(models.Model):
    last_updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey('auth.User', editable=False)
    entrance_id = models.CharField(max_length=255)
    exit_url = models.TextField(max_length=255)
    start_time = models.DateTimeField(blank=True, null=True)
    finish_time = models.DateTimeField(blank=True, null=True)
    survey_path_id = models.IntegerField(blank=True)  # For auditing
    last_screen_id = models.IntegerField(default=0)

    # Demographic Data
    age = models.IntegerField(blank=True, null=True)
    education = models.CharField(blank=True, null=True, choices=EDUCATION_CHOICES, max_length=200)
    household_income = models.CharField(blank=True, null=True, choices=HOUSEHOLD_INCOME_CHOICES, max_length=200)
    diagnosed_with_serious_mental_illness = models.BooleanField(default=False)
    diagnosed_with_schizophrenia = models.BooleanField(default=False)
    diagnosed_with_depression = models.BooleanField(default=False)
    diagnosed_with_bipolar = models.BooleanField(default=False)
    diagnosed_with_other = models.BooleanField(default=False)
    diagnosed_with_dont_know = models.BooleanField(default=False)
    family_diagnosed_with_serious_mental_illness = models.BooleanField(default=False)
    family_diagnosed_with_schizophrenia = models.BooleanField(default=False)
    family_diagnosed_with_depression = models.BooleanField(default=False)
    family_diagnosed_with_bipolar = models.BooleanField(default=False)
    family_diagnosed_with_other = models.BooleanField(default=False)
    family_diagnosed_with_dont_know = models.BooleanField(default=False)
    demographics_complete = models.BooleanField(default=False)

    state_1 = models.ForeignKey(HealthState, blank=True, null=True, related_name='+', on_delete=models.PROTECT)
    state_2 = models.ForeignKey(HealthState, blank=True, null=True, related_name='+', on_delete=models.PROTECT)
    state_3 = models.ForeignKey(HealthState, blank=True, null=True, related_name='+', on_delete=models.PROTECT)
    state_4 = models.ForeignKey(HealthState, blank=True, null=True, related_name='+', on_delete=models.PROTECT)
    state_5 = models.ForeignKey(HealthState, blank=True, null=True, related_name='+', on_delete=models.PROTECT)
    state_6 = models.ForeignKey(HealthState, blank=True, null=True, related_name='+', on_delete=models.PROTECT)
    state_7 = models.ForeignKey(HealthState, blank=True, null=True, related_name='+', on_delete=models.PROTECT)
    state_8 = models.ForeignKey(HealthState, blank=True, null=True, related_name='+', on_delete=models.PROTECT)

    def __unicode__(self):
        return "User %s" % self.entrance_id

    def save(self, *args, **kwargs):
        created = False
        if not self.id:
            created = True
            path = SurveyPath.get_next_path()
            self.survey_path_id = path.pk

        super(SurveyResponse, self).save(*args, **kwargs)

        if created:
            for i in range(1, 9):
                hs = HealthState.objects.get(number=getattr(path, "state_%s" % i))
                setattr(self, "state_%s" % i, hs)
                HealthStateRating.objects.create(survey_response=self, health_state=hs, order=i)

    @property
    def ratings(self):
        return self.healthstaterating_set.all()

    @property
    def percent_complete(self):
        return 100.0 * self.last_screen_id / len(SCREENS)

    def get_screen_for(self, screen_id):
        for s in SCREENS:
            if s["id"] == screen_id:
                return s
        return None

    def mark_screen_complete(self, screen_id):
        s = self.get_screen_for(screen_id)
        if s:
            if s["order"] > self.last_screen_id:
                self.last_screen_id = s["order"]
                self.save()
        else:
            raise Exception("mark_screen_complete called for %s, which isn't a valid id." % screen_id)

    @property
    def current_health_state_number(self):
        for i in range(1, 9):
            if not self._completed_state(i):
                return i
        return None

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

    # For the admin
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

    def _started_state(self, order):
        try:
            return self.ratings.get(order=order).started()
        except HealthStateRating.DoesNotExist:
            return False

    def started_state_1(self):
        return self._started_state(1)

    def started_state_2(self):
        return self._started_state(2)

    def started_state_3(self):
        return self._started_state(3)

    def started_state_4(self):
        return self._started_state(4)

    def started_state_5(self):
        return self._started_state(5)

    def started_state_6(self):
        return self._started_state(6)

    def started_state_7(self):
        return self._started_state(7)

    def started_state_8(self):
        return self._started_state(8)

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

    intro_completed = models.BooleanField(default=False)
    intro_completed_time = models.DateTimeField(blank=True, null=True)

    video_completed = models.BooleanField(default=False)
    video_completed_time = models.DateTimeField(blank=True, null=True)

    vas_completed = models.BooleanField(default=False)
    vas_completed_time = models.DateTimeField(blank=True, null=True)

    tto_completed = models.BooleanField(default=False)
    tto_completed_time = models.DateTimeField(blank=True, null=True)

    outro_completed = models.BooleanField(default=False)
    outro_completed_time = models.DateTimeField(blank=True, null=True)

    def started(self):
        return self.start_time is not None

    def finished(self):
        return self.finish_time is not None

    started.boolean = True
    finished.boolean = True


class SurveyAggregateStats(models.Model):
    completion_rate = models.FloatField(blank=True, null=True)
    average_survey_progress = models.FloatField(blank=True, null=True)
    dwell_time = models.FloatField(blank=True, null=True)

    @classmethod
    def first(cls):
        if cls.objects.count() > 0:
            return cls.objects.all()[0]
        else:
            update_aggregate_tasks()
            return cls.first


def export_filename(instance, filename):
    return "exports/Export-%s.csv" % instance.export_date.isoformat(" ")


class SurveyExport(models.Model):
    csv_file = models.FileField(blank=True, null=True, upload_to=export_filename)
    num_rows = models.IntegerField()
    export_date = models.DateTimeField(auto_now_add=True)


class ActionLog(models.Model):
    user = models.ForeignKey('auth.User')
    when = models.DateTimeField(auto_now_add=True)
    action = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return "%s - %s" % (self.action, self.user)

# Patch to prevent superuser delete
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver
from django.contrib.auth.models import User
from django.core.exceptions import PermissionDenied

@receiver(pre_delete, sender=User)
def delete_user(sender, instance, **kwargs):
    if instance.is_superuser:
        raise PermissionDenied