from django.conf import settings
from django.http import HttpResponseRedirect


class ForceAuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_authenticated:
            if '/auth/' not in request.path:
                if request.path != settings.LOGIN_URL:
                    return HttpResponseRedirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
        return self.get_response(request)