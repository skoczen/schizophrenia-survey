from annoying.decorators import render_to
from django.contrib.auth.decorators import user_passes_test

from survey.forms import HealthStateSequenceUploadForm
from survey.tasks import update_health_sequences


@user_passes_test(lambda u: u.groups.filter(name='Survey Super-Admins').count() == 1)
@render_to("survey/administration/upload_sequence.html")
def upload_sequence(request):
    uploaded = False
    if request.method == "POST":
        form = HealthStateSequenceUploadForm(request.POST, request.FILES)

        if form.is_valid():
            upload = form.save()
            update_health_sequences(upload.pk)
            uploaded = True
    else:
        form = HealthStateSequenceUploadForm()
    return locals()


@user_passes_test(lambda u: u.groups.filter(name='Survey Administrators').count() == 1)
@render_to("survey/administration/dashboard.html")
def dashboard(request):
    return locals()
