from annoying.decorators import render_to
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth import login, authenticate

from .models import SurveyResponse
from django.contrib.auth.models import User

@render_to("survey/entrance.html")
def entrance(request):
    try:
        survey_id = request.REQUEST["survey_id"]
        exit_url = request.REQUEST["exit_url"]

        if User.objects.filter(username=survey_id).count() > 0:
            if not request.user.is_authenticated():
                user = authenticate(username=survey_id, password=survey_id)
                login(request, user)
            else:
                user = request.user
        else:
            user = User.objects.create(username=survey_id)
            user.set_password(survey_id)
            user.save()
            user = authenticate(username=survey_id, password=survey_id)
            login(request, user)

        survey_response = SurveyResponse.objects.get_or_create(entrance_id=survey_id, user=user)[0]
        survey_response.exit_url = exit_url
        survey_response.save()

    except:
        import traceback; traceback.print_exc();
        return HttpResponseRedirect(reverse("survey:unknown_code"))
    return locals()

def next_page(request):
    return HttpResponseRedirect(reverse("survey:in_survey_stub"))

@render_to("survey/in_survey_stub.html")
def in_survey_stub(request):
    try:
        survey_response = SurveyResponse.objects.get(user=request.user)
    except:
        return HttpResponseRedirect(reverse("survey:unknown_code"))
    return locals()


@render_to("survey/unknown_code.html")
def unknown_code(request):
    return locals()
