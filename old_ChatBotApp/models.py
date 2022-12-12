from django.db import models

# Create your models here.
class ChatBotModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    # チャットbot名のデータが必要かもしれない
    # 後で: チャットbotのアイコン画像パスが必要かもしれない
    def __str__(self):
        return f'type{self.chat_bot_type}'