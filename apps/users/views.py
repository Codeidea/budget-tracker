from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import login
from django.shortcuts import render
from django.views.generic.base import View


class LoginView(View):
    def get(self, request):
        return login(request, authentication_form=AuthenticationForm)

    def post(self, request):
        if not request.POST.get('remember_me', None):
            request.session.set_expiry(0)
        else:
            #TODO move expiration time to SETTINGS
            request.session.set_expiry(3600*24*14)
        return login(request, authentication_form=AuthenticationForm)