from annoying.decorators import render_to
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from survey.models import SurveyAggregateStats, SurveyExport, ActionLog, SurveyConfig
from survey.forms import HealthStateSequenceUploadForm, SurveyConfigForm
from survey.tasks import update_health_sequences, generate_csv


@user_passes_test(lambda u: u.groups.filter(name='Survey Super-Admins').count() == 1)
@render_to("survey/administration/upload_sequence.html")
def upload_sequence(request):
    section = "upload_sequence"
    ActionLog.objects.create(user=request.user, action="Upload Sequence Visit")
    uploaded = False
    if request.method == "POST":
        form = HealthStateSequenceUploadForm(request.POST, request.FILES)

        if form.is_valid():
            upload = form.save()
            update_health_sequences(upload.pk)
            uploaded = True
            ActionLog.objects.create(user=request.user, action="New Sequence Uploaded")
    else:
        form = HealthStateSequenceUploadForm()
    return locals()

@user_passes_test(lambda u: u.groups.filter(name='Survey Super-Admins').count() == 1)
@render_to("survey/administration/survey_config.html")
def survey_config(request):
    section = "survey_config"
    survey_config = SurveyConfig.first()
    ActionLog.objects.create(user=request.user, action="Survey Config Visit")
    saved = False
    if request.method == "POST":
        form = SurveyConfigForm(request.POST, request.FILES, instance=survey_config)

        if form.is_valid():
            survey_config = form.save()
            saved = True
            ActionLog.objects.create(user=request.user, action="Survey Config Changed")
    else:
        form = SurveyConfigForm(instance=survey_config)
    return locals()



@user_passes_test(lambda u: u.groups.filter(name='Survey Administrators').count() == 1)
@render_to("survey/administration/dashboard.html")
def dashboard(request):
    section = "dashboard"
    stats = SurveyAggregateStats.first
    ActionLog.objects.create(user=request.user, action="Dashboard View")
    return locals()


@user_passes_test(lambda u: u.groups.filter(name='Survey Super-Admins').count() == 1)
@render_to("survey/administration/data_export.html")
def data_export(request):
    section = "data_export"
    data_exports = SurveyExport.objects.all().order_by("-export_date")
    ActionLog.objects.create(user=request.user, action="Data Export Visit")
    return locals()


@user_passes_test(lambda u: u.groups.filter(name='Survey Super-Admins').count() == 1)
def generate_new_export(request):
    generate_csv()
    ActionLog.objects.create(user=request.user, action="New Export Generated")
    return HttpResponseRedirect(reverse("survey:admin_data_export"))
