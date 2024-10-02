# chat/admin.py

from django.contrib import admin
from .models import GroupChat, Message, UserProfile

# Регистрация модели GroupChat в админке
admin.site.register(GroupChat)
admin.site.register(Message)
admin.site.register(UserProfile)