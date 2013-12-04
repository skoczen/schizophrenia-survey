import datetime

from annoying.decorators import render_to
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate

from survey.forms import HealthStateSequenceUploadForm, DemographicForm
from survey.models import SurveyResponse
from survey.screens import SCREENS
from survey.tasks import update_health_sequences
from django.contrib.auth.models import User


def temp_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse("survey:entrance"))


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

        survey_response, created = SurveyResponse.objects.get_or_create(user=user)
        if created:
            survey_response.start_time = datetime.datetime.now()
            survey_response.save()
        if survey_id:
            survey_response.entrance_id = survey_id
        if exit_url:
            survey_response.exit_url = exit_url
        survey_response.save()

        if survey_response.finished():
            return HttpResponseRedirect(reverse("survey:complete"))
        if not created and survey_response.started():
            return HttpResponseRedirect(reverse("survey:in_survey"))

    except:
        return HttpResponseRedirect(reverse("survey:unknown_code"))
    return locals()


def next_page(request):
    try:
        survey_response = SurveyResponse.objects.get(user=request.user)
        if not survey_response.demographics_complete:
            if request.method == "POST":
                form = DemographicsForm(request.POST, instance=survey_response)
                if form.is_valid():
                    survey_response = form.save()
                    survey_response.demographics_complete = True
                    survey_response.save()
                else:
                    return HttpResponseRedirect(reverse("survey:demographics"))
            else:
                return HttpResponseRedirect(reverse("survey:demographics"))

        if "complete" in request.GET:
            hsr = survey_response.current_health_state_rating
            hsr.finish_time = datetime.datetime.now()
            hsr.save()
        if survey_response.completed_state_8():
            survey_response.finish_time = datetime.datetime.now()
            survey_response.save()
        if survey_response.finished():
            return HttpResponseRedirect(reverse("survey:complete"))
    except:
        return HttpResponseRedirect(reverse("survey:unknown_code"))
    return HttpResponseRedirect(reverse("survey:in_survey"))


@render_to("survey/health_state.html")
def demographics(request):
    try:
        survey_response = SurveyResponse.objects.get(user=request.user)
        form = DemographicsForm(instance=survey_response)
        context = locals()
        context.update(survey_response.current_page_context)
    except:
        return HttpResponseRedirect(reverse("survey:unknown_code"))
    return context


@render_to("survey/health_state.html")
def in_survey(request):
    try:
        survey_response = SurveyResponse.objects.get(user=request.user)
        context = locals()
        context.update(survey_response.current_page_context)
    except:
        return HttpResponseRedirect(reverse("survey:unknown_code"))
    return context


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