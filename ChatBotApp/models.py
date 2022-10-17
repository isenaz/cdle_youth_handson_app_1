from django.db import models

# Create your models here.
class ChatBotModel(models.Model):
    chat_bot_type = models.IntegerField()
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)