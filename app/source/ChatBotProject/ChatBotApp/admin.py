from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users, ChatContentModel
from django.contrib.auth import get_user_model

# User = get_user_model()

# # Register your models here.
# admin.site.register(User)

admin.site.register(ChatContentModel)