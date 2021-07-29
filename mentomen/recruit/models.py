from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    member = models.IntegerField(default=1)
    field = models.CharField(max_length=50, default="분야")
    pub_date = models.DateTimeField(default=timezone.now)
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    def __str__(self):
        return self.postname
