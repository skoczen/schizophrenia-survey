import datetime

from annoying.decorators import render_to
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate

from survey.forms import HealthStateSequenceUploadForm, DemographicForm, VASForm, TTOForm
from survey.models import SurveyResponse, SurveyConfig
from survey.screens import SCREENS
from survey.tasks import update_health_sequences
from django.contrib.auth.models import User


def temp_logout(request):
    from utils.factory import Factory
    logout(request)
    return HttpResponseRedirect("%s?exit_url=http://a.com&survey_id=%s" % (reverse("survey:entrance"), Factory.rand_int(start=100000000, end=999999999)))


@render_to("survey/entrance.html")
def entrance(request):
    try:
        survey_id = None
        exit_url = None
        section = "intro"
        screen = SCREENS[0]
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
        if survey_response.last_screen_id != 0:
            return HttpResponseRedirect(reverse("survey:go_to_current"))
    except:
        return HttpResponseRedirect(reverse("survey:unknown_code"))
    survey_config = SurveyConfig.first()
    return locals()


def next_screen(request, last_screen_id=None):
    try:
        
        if last_screen_id:
            screen = SCREENS[int(last_screen_id) + 1]
        else:
            survey_response = SurveyResponse.objects.get(user=request.user)
            screen = SCREENS[survey_response.last_screen_id + 1]
        return HttpResponseRedirect(reverse(screen["reverse_url"], args=screen["reverse_args"]))
    except SurveyResponse.DoesNotExist:
        return HttpResponseRedirect(reverse("survey:unknown_code"))


def go_to_current(request):
    try:
        survey_response = SurveyResponse.objects.get(user=request.user)
        screen = SCREENS[survey_response.last_screen_id + 1]
        return HttpResponseRedirect(reverse(screen["reverse_url"], args=screen["reverse_args"]))
    except SurveyResponse.DoesNotExist:
        return HttpResponseRedirect(reverse("survey:unknown_code"))


def specific_screen(request):
    survey_response = SurveyResponse.objects.get(user=request.user)
    if "screen_id" in request.GET:
        screen_id = int(request.GET["screen_id"])
        if screen_id <= survey_response.last_screen_id + 1:
            screen = SCREENS[screen_id]
            return HttpResponseRedirect(reverse(screen["reverse_url"], args=screen["reverse_args"]))

    return HttpResponseRedirect(reverse("survey:go_to_current"))


@render_to("survey/about.html")
def about(request):
    try:
        section = "about"
        screen = SCREENS[0]
        survey_response = SurveyResponse.objects.get(user=request.user)
        survey_config = SurveyConfig.first()
    except:
        pass
    return locals()


@render_to("survey/demographics.html")
def demographics(request):
    try:
        section = "intro"
        screen = SCREENS[1]
        survey_response = SurveyResponse.objects.get(user=request.user)
        survey_config = SurveyConfig.first()
        survey_response.mark_screen_complete("entrance")
        if request.method == "POST":
            form = DemographicForm(request.POST, instance=survey_response)
            if form.is_valid():
                survey_response = form.save()
                survey_response.demographics_complete = True
                survey_response.save()
                survey_response.mark_screen_complete("demographics")
                return HttpResponseRedirect(reverse("survey:go_to_current"))
        else:
            form = DemographicForm(instance=survey_response)
        context = locals()
    except:
        import traceback; traceback.print_exc();
        return HttpResponseRedirect(reverse("survey:unknown_code"))
    return context

def read_only_screen(request, screen_complete_name, mark_complete=True):
    try:

        survey_response = SurveyResponse.objects.get(user=request.user)
        survey_config = SurveyConfig.first()
        screen = survey_response.get_screen_for(screen_complete_name)
        is_current_screen = SCREENS[survey_response.last_screen_id + 1] == screen
        if screen["order"] > survey_response.last_screen_id + 1:
            return HttpResponseRedirect(reverse("survey:go_to_current"))

        context = locals()
        if mark_complete:
            survey_response.mark_screen_complete(screen_complete_name)

    except:
        import traceback; traceback.print_exc();
        return HttpResponseRedirect(reverse("survey:unknown_code"))
    return context


@render_to("survey/introduction.html")
def introduction(request):
    context = read_only_screen(request, "introduction")
    context['section'] = "intro"
    return context

@render_to("survey/vas_training.html")
def vas_training(request):
    context = read_only_screen(request, "vas_training")
    context['section'] = "training"
    return context

@render_to("survey/tto_training.html")
def tto_training(request):
    context = read_only_screen(request, "tto_training")
    context['section'] = "training"
    return context

def health_state_screen(request, section, health_state_number, mark_complete=True):
    now = datetime.datetime.now()
    context = read_only_screen(request, "hs%s_%s" % (health_state_number, section), mark_complete=mark_complete)
    if isinstance(context, dict):
        sr = context["survey_response"]
        health_state = getattr(sr, "state_%s" % health_state_number)
        health_state_rating = sr.ratings.get(health_state=health_state)

        if health_state_rating.start_time is None:
            health_state_rating.start_time = now
        if mark_complete:
            setattr(health_state_rating, "%s_completed" % section, True)
            setattr(health_state_rating, "%s_completed_time" % section, now)
            if section == "outro":
                health_state_rating.finish_time = now
        health_state_rating.save()

        context['health_state'] = health_state
        context['health_state_rating'] = health_state_rating
        context['section'] = "hs_%s" % health_state_number
    return context


@render_to("survey/health_state_intro.html")
def health_state_intro(request, health_state_number):
    return health_state_screen(request, "intro", health_state_number)


@render_to("survey/health_state_video.html")
def health_state_video(request, health_state_number):
    return health_state_screen(request, "video", health_state_number)


@render_to("survey/health_state_vas.html")
def health_state_vas(request, health_state_number):
    base_context = health_state_screen(request, "vas", health_state_number, mark_complete=False)
    hsr = base_context["health_state_rating"]
    hsr.video_watched = True
    hsr.video_completed_time = datetime.datetime.now()
    hsr.save()
    base_context["health_state_rating"] = hsr

    if request.method == "POST":
        form = VASForm(request.POST, instance=base_context["health_state_rating"])
        if form.is_valid():
            form.save()

            # Mark complete
            health_state_screen(request, "vas", health_state_number)
            return HttpResponseRedirect(reverse("survey:next_screen", args=(base_context["screen"]["order"], )))
    else:
        form = VASForm(instance=base_context["health_state_rating"])

    base_context.update(locals())
    return base_context


@render_to("survey/health_state_tto.html")
def health_state_tto(request, health_state_number):
    base_context = health_state_screen(request, "tto", health_state_number, mark_complete=False)

    if request.method == "POST":
        form = TTOForm(request.POST, instance=base_context["health_state_rating"])
        if form.is_valid():
            form.save()

            # Mark complete
            health_state_screen(request, "tto", health_state_number)
            return HttpResponseRedirect(reverse("survey:next_screen", args=(base_context["screen"]["order"], )))
    else:
        form = TTOForm(instance=base_context["health_state_rating"])

    base_context.update(locals())
    return base_context


@render_to("survey/health_state_outro.html")
def health_state_outro(request, health_state_number):
    return health_state_screen(request, "outro", health_state_number)

@render_to("survey/complete.html")
def complete(request):
    try:
        screen = SCREENS[-1]
        survey_response = SurveyResponse.objects.get(user=request.user)
        survey_response.finish_time = datetime.datetime.now()
        survey_response.save()
    except:
        return HttpResponseRedirect(reverse("survey:unknown_code"))
    return locals()


@render_to("survey/unknown_code.html")
def unknown_code(request):
    return locals()

