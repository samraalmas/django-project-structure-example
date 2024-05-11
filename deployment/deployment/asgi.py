import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels_with_celery import routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "deployment.settings.development")
print("asgiiii")
application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Django HTTP ASGI application
    "websocket": URLRouter(
        routing.websocket_urlpatterns
    ),  # Django Channels WebSocket routing
})

