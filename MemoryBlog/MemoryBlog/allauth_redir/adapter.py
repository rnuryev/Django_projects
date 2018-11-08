from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from django.http import HttpRequest

class MyAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        path = request.META['HTTP_REFERER']
        return path.format(username=request.user.username)

    def get_logout_redirect_url(self, request):
        path = request.META['HTTP_REFERER']
        return path.format(username=request.user.username)