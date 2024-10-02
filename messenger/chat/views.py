# chat/views.py

from rest_framework import viewsets
from .models import GroupChat, Message, UserProfile
from .serializers import GroupChatSerializer, MessageSerializer, UserProfileSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render


class GroupChatViewSet(viewsets.ModelViewSet):
    queryset = GroupChat.objects.all()
    serializer_class = GroupChatSerializer
    permission_classes = [IsAuthenticated]

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

def index(request):
    return render(request, 'chat/index.html')