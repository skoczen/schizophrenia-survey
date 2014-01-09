class GroupMiddleware(object):

    def process_request(self, request):
        if "administration" in request.path_info:
            request.session['survey_admin'] = request.user.groups.filter(name='Survey Administrators').count() == 1
            request.session['survey_superadmin'] = request.user.groups.filter(name='Survey Super-Admins').count() == 1
