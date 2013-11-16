from annoying.decorators import render_to
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


@render_to("survey/entrance.html")
def entrance(request):
    try:
        survey_id = request.REQUEST["survey_id"]
        exit_url = request.REQUEST["exit_url"]
    except:
        return HttpResponseRedirect(reverse("survey:unknown_code"))
    return locals()


@render_to("survey/unknown_code.html")
def unknown_code(request):
    return locals()
