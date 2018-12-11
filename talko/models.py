from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    text = models.TextField(max_length=1000)
    date = models.DateTimeField(auto_now=True)
    sender = models.ForeignKey(User, related_name='sender', on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name='receiver', on_delete=models.CASCADE)

    def __str__(self):
        return self.text