from django.db import models
from django.contrib.auth.models import User


def __str__(self):
    return self.user.usrname


class Message(models.Model):
    text = models.TextField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)