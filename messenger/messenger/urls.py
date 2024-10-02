# messenger/urls.py

from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
	openapi.Info(
		title="Messenger API",
		default_version='v1',
		description="API documentation for Messenger application",
		terms_of_service="https://www.google.com/policies/terms/",
		contact=openapi.Contact(email="contact@messenger.local"),
		license=openapi.License(name="BSD License"),
	),
	public=True,
)

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('chat.urls')),  # Добавляем путь для корневого URL (если нужно)

	# Swagger URLs:
	path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),  # Swagger UI
]