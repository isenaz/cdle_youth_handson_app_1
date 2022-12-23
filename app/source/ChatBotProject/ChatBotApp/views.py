from django.shortcuts import render
from .forms import RegistForm, UserLoginForm
from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView, View
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.shortcuts import redirect

class RegistUserView(CreateView):
    template_name = "login/register.html"
    form_class = RegistForm
    
    def form_invalid(self, form):
        # エラーからメッセージのみを取り出す
        values = form.errors.get_json_data().values()
        for value in values:
            for v in value:
                messages.add_message(self.request, messages.WARNING, v["message"]) # formのerrorを追加
        
        messages.add_message(self.request, messages.ERROR, "アカウントの作成に失敗しました。")
        return super().form_invalid(form)
        
    
class UserLoginView(LoginView):
    template_name = "login/login.html"
    authentication_form = UserLoginForm
    
    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "ログインに失敗しました。正しいメールアドレスとパスワードを入力してください。")
        return super().form_invalid(form)
    
    
class UserLogoutView(LogoutView):
    pass
    

class MyPageView(LoginRequiredMixin, TemplateView):
    template_name = "rooms/my_page.html"
    