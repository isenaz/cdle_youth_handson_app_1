from django.shortcuts import render
from .forms import RegistForm, UserLoginForm, UserPasswordResetForm, UserSetPasswordForm
from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView, View
from django.contrib.auth.views import (
    LoginView, LogoutView, 
    PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView, PasswordResetConfirmView
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy

class RegistUserView(CreateView):
    template_name = "login/register.html"
    form_class = RegistForm
    success_url = reverse_lazy("chatbot_app:login")
    
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
    
class UserPasswordReset(PasswordResetView):
    template_name = "login/password_reset.html"
    email_template_name = "login/password_reset/message.txt" # メールの中身
    subject_template_name = "login/password_reset/subject.txt" # メールタイトル
    form_class = UserPasswordResetForm
    success_url = reverse_lazy("chatbot_app:password_reset_done")
    
    def form_invalid(self, form):
        values = form.errors.get_json_data().values()
        for value in values:
            for v in value:
                messages.add_message(self.request, messages.WARNING, v["message"]) # formのerrorを追加
        messages.add_message(self.request, messages.ERROR, "もう一度メールアドレスを入力してください。")
        return super().form_invalid(form)
    

class UserPasswordResetDone(PasswordResetDoneView):
    template_name = "login/password_reset_done.html"


class UserPasswordResetConfirm(PasswordResetConfirmView):
    template_name = "login/password_reset_confirm.html"
    form_class = UserSetPasswordForm
    success_url  = reverse_lazy("chatbot_app:password_reset_complete")
    
    def form_invalid(self, form):
        values = form.errors.get_json_data().values()
        for value in values:
            for v in value:
                messages.add_message(self.request, messages.WARNING, v["message"]) # formのerrorを追加
        messages.add_message(self.request, messages.ERROR, "もう一度パスワードを入力してください")
        return super().form_invalid(form)
    
class UserPasswordResetComplete(PasswordResetCompleteView):
    template_name = "login/password_reset_complete.html"


class MyPageView(LoginRequiredMixin, TemplateView):
    template_name = "rooms/my_page.html"
    