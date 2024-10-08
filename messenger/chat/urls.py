# chat/urls.py

from django.urls import path, include
from .views import GroupChatViewSet, MessageViewSet, UserProfileViewSet, index  # Импортируем ваши представления
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'groupchats', GroupChatViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'profiles', UserProfileViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('api/', include(router.urls)),  # API маршруты
]