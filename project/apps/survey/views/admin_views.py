from annoying.decorators import render_to
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from survey.models import SurveyAggregateStats, SurveyExport, ActionLog
from survey.forms import HealthStateSequenceUploadForm
from survey.tasks import update_health_sequences, generate_csv


@user_passes_test(lambda u: u.groups.filter(name='Survey Super-Admins').count() == 1)
@render_to("survey/administration/upload_sequence.html")
def upload_sequence(request):
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


@user_passes_test(lambda u: u.groups.filter(name='Survey Administrators').count() == 1)
@render_to("survey/administration/dashboard.html")
def dashboard(request):
    stats = SurveyAggregateStats.first
    ActionLog.objects.create(user=request.user, action="Dashboard View")
    return locals()


@user_passes_test(lambda u: u.groups.filter(name='Survey Super-Admins').count() == 1)
@render_to("survey/administration/data_export.html")
def data_export(request):
    data_exports = SurveyExport.objects.all().order_by("-export_date")
    ActionLog.objects.create(user=request.user, action="Data Export Visit")
    return locals()


@user_passes_test(lambda u: u.groups.filter(name='Survey Super-Admins').count() == 1)
def generate_new_export(request):
    generate_csv()
    ActionLog.objects.create(user=request.user, action="New Export Generated")
    return HttpResponseRedirect(reverse("survey:admin_data_export"))
