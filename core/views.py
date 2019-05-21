from django.views.generic import View
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class UserLogin(View):
    """
    User Login View.
    """

    def get(self, request):
        return render(request, 'login.html')


class Home(View):
    """
    User Home page after successful login.
    """

    @method_decorator(login_required)
    def get(self, request):
        return render(request, 'home.html')
