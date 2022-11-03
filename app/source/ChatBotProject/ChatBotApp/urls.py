from django.urls import path
from .views import (
    RegistUserView, UserLoginView, UserLogoutView, MyPageView
)

app_name = "chatbot_app"
urlpatterns = [
    path("regist/", RegistUserView.as_view(), name="regist"),
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", UserLogoutView.as_view(), name="logout"),
    path("my_page/", MyPageView.as_view(), name="my_page"),
]
