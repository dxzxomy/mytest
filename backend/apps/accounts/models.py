from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # 如果定制User，需要在Settings配置AUTH_USER_MODEL
    # CharField => max_length
    # ImageFiled => Pillow 库
    mobile = models.CharField(max_length=11, verbose_name="手机号",default='')