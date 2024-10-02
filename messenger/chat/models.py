# chat/models.py

from django.db import models
from django.contrib.auth.models import User

class GroupChat(models.Model):
    name = models.CharField(max_length=255)
    members = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    group_chat = models.ForeignKey(GroupChat, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
