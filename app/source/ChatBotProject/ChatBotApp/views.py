from django.shortcuts import render
from .forms import RegistForm, UserLoginForm
from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin

class RegistUserView(CreateView):
    template_name = "login/register.html"
    form_class = RegistForm
    
class UserLoginView(LoginView):
    template_name = "login/login.html"
    authentication_form = UserLoginForm
    
class UserLogoutView(LogoutView):
    pass
    

class MyPageView(LoginRequiredMixin, TemplateView):
    template_name = "rooms/my_page.html"
    