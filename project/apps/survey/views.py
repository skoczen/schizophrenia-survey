import datetime

from annoying.decorators import render_to
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate

from .forms import HealthStateSequenceUploadForm
from .models import SurveyResponse
from .tasks import update_health_sequences
from django.contrib.auth.models import User


@render_to("survey/entrance.html")
def entrance(request):
    try:
        survey_id = None
        exit_url = None
        if not request.user.is_authenticated():
            survey_id = request.REQUEST["survey_id"]
            exit_url = request.REQUEST["exit_url"]

            if User.objects.filter(username=survey_id).count() > 0:
                user = authenticate(username=survey_id, password=survey_id)
                login(request, user)
            else:
                user = User.objects.create(username=survey_id)
                user.set_password(survey_id)
                user.save()
                user = authenticate(username=survey_id, password=survey_id)
                login(request, user)
        else:
            user = request.user

        survey_response = SurveyResponse.objects.get_or_create(user=user)[0]
        if survey_id:
            survey_response.entrance_id = survey_id
        if exit_url:
            survey_response.exit_url = exit_url
        survey_response.save()

        if survey_response.finished():
            return HttpResponseRedirect(reverse("survey:complete"))
        if survey_response.started():
            return HttpResponseRedirect(reverse("survey:in_survey_stub"))

    except:
        import traceback; traceback.print_exc();
        return HttpResponseRedirect(reverse("survey:unknown_code"))
    return locals()


def next_page(request):
    try:
        survey_response = SurveyResponse.objects.get(user=request.user)
        if survey_response.finished():
            return HttpResponseRedirect(reverse("survey:complete"))
    except:
        return HttpResponseRedirect(reverse("survey:unknown_code"))
    return HttpResponseRedirect(reverse("survey:in_survey_stub"))


@render_to("survey/in_survey_stub.html")
def in_survey_stub(request):
    try:
        survey_response = SurveyResponse.objects.get(user=request.user)
        survey_response.start_time = datetime.datetime.now()
        survey_response.save()
    except:
        return HttpResponseRedirect(reverse("survey:unknown_code"))
    return locals()


@render_to("survey/complete.html")
def complete(request):
    try:
        survey_response = SurveyResponse.objects.get(user=request.user)
        survey_response.finish_time = datetime.datetime.now()
        survey_response.save()
    except:
        return HttpResponseRedirect(reverse("survey:unknown_code"))
    return locals()


@render_to("survey/unknown_code.html")
def unknown_code(request):
    return locals()


@user_passes_test(lambda u: u.groups.filter(name='Survey Super-Admins').count() == 1, login_url='/administration/')
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