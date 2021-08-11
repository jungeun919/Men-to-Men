from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class CustomUser(AbstractUser):
    major = models.CharField(max_length=50, null=True) # 전공
    grade = models.IntegerField(null=True) # 학번(ex. 19/20/21)