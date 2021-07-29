from django.db import models
from django.utils import timezone
from django.contrib.auth import settings

# Create your models here.
class Post(models.Model):
    member = models.IntegerField(default=1)
    field = models.CharField(max_length=50, default="분야")
    pub_date = models.DateTimeField(default=timezone.now)
    postname = models.CharField(max_length=50)
    contents = models.TextField()

    def __str__(self):
        return self.postname

class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name="comments")
    co_writer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()

    def __str__(self):
        return self.text