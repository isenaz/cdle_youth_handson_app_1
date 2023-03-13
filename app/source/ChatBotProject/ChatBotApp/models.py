from django.db import models
from django.contrib.auth.models import(
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.urls import reverse_lazy
# Create your models here.
class UserManager(BaseUserManager):
    # データを挿入するクラス
    def create_user(self, username, email, password=None):
        if not email:
            raise ValueError("メールアドレスを入力してください")
        
        if not username: 
            raise ValueError("ユーザーネームを入力してください")
        
        
        user = self.model(
            username=username,
            email=email
        )
        user.set_password(password)
        user.save(using=self._db) # DBにユーザーを保存
        return user

    def create_superuser(self, username, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.model(
            username = username,
            email = email,
        )
        user.set_password(password)
        user.is_staff = True
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Users(AbstractBaseUser, PermissionsMixin):
    #テーブルを定義するクラス
    
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    image_url = models.CharField(max_length=255, default=False) 
    is_active = models.BooleanField(default=True) # 後でactiveを操作するクラスを作成して、デフォルトをFalseにする
    is_staff = models.BooleanField(default=False)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    objects = UserManager()
    
    def get_absolute_url(self):
        return reverse_lazy("chatbot_app:regist")

class ChatBotModel(models.Model):
    # チャットbotのデータに関するクラス
    
    name = models.CharField(max_length=255)

class ChatContentModel(models.Model):
    # チャットの会話内容に関するクラス

    user_name = models.CharField(max_length=255)
    chatbot_name = models.ManyToManyField(ChatBotModel) # Check
    content = models.TextField()