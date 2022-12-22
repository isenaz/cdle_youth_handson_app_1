from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class RegistForm(forms.ModelForm):
    username = forms.CharField(label="ユーザーネーム")
    email = forms.EmailField(label="メールアドレス")
    password = forms.CharField(label="パスワード", widget=forms.PasswordInput())
    
    class Meta:
        model = Users
        fields = ["username", "email", "password"]

    # saveメソッドをカスタマイズ（パスワードのバリデーションを追加）
    def save(self, commit=False):
        user = super().save(commit=False)
        validate_password(self.cleaned_data["password"], user) # passwordが正しいかバリデーションを行う
        user.set_password(self.cleaned_data["password"])
        user.save()
        return user
    
class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="メールアドレス")
    password = forms.CharField(label="パスワード",
                               widget=forms.PasswordInput())