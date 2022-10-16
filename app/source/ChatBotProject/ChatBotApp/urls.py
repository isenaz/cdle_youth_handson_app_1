from django.urls import path
from .views import (
    RegistUserView
)

app_name = "chatbot_app"
urlpatterns = [
    path("regist/", RegistUserView.as_view(), name="regist")
]
