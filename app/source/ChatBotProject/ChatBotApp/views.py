from django.shortcuts import render
from .forms import RegistForm
from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView, View

class RegistUserView(CreateView):
    template_name = "login/register.html"
    form_class = RegistForm
    
# class UserLoginView(LoginView):
    # template_name = "user_login.html"
    # authentication_form = UserLoginForm
    
    