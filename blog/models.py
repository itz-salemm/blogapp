from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Content(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    authur = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title