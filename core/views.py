from django.views.generic import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class UserLogin(View):

    def get(self, request):
        return render(request, 'login.html')


class Home(View):

    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'home.html')
