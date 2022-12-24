from django.urls import path
from .views import (
    RegistUserView, UserLoginView, UserLogoutView, MyPageView,
    UserPasswordReset, UserPasswordResetDone, UserPasswordResetConfirm, USerPasswordResetComplete
)

app_name = "chatbot_app"
urlpatterns = [
    path("regist/", RegistUserView.as_view(), name="regist"),
    path("", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("mypage/", MyPageView.as_view(), name="mypage"),
    path("password_reset/", UserPasswordReset.as_view(), name="password_reset"),
    path("password_reset/done/", UserPasswordResetDone.as_view(), name="password_reset_done"),
    path("password_reset/confirm/<uidb64>/<token>/", UserPasswordResetConfirm.as_view(), name="password_reset_confirm"),
    path("password_reset/complete/", USerPasswordResetComplete.as_view(), name="password_reset_complete"),
]
