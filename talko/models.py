from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    text = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username