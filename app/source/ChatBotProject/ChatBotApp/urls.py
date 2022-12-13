from django.urls import path
from .views import (
    RegistUserView, UserLoginView, UserLogoutView, MyPageView, ChatBotView
)

app_name = "chatbot_app"
urlpatterns = [
    path("regist/", RegistUserView.as_view(), name="regist"),
    path("", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("mypage/", MyPageView.as_view(), name="mypage"),
    path("chat/", ChatBotView.as_view(), name='chatbot'), 
]
