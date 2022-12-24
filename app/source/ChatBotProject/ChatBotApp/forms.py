from django import forms
from .models import Users
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm
from django.core.exceptions import ValidationError
import re



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
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data["password"]
        if len(password) < 8:
            raise forms.ValidationError("パスワードは8文字以上です。")
        if not re.search(r"\d+", password):
            raise forms.ValidationError("パスワードに数字が含まれていません。")
        elif not re.search(r"[A-Za-z]+", password):
            raise forms.ValidationError("パスワードにアルファベットが含まれていません。")
    
class UserLoginForm(AuthenticationForm):
    username = forms.EmailField(label="メールアドレス")
    password = forms.CharField(label="パスワード",
                               widget=forms.PasswordInput())
    
class UserPasswordResetForm(PasswordResetForm):
    pass

class UserSetPasswordForm(SetPasswordForm):
    pass