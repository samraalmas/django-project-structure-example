# routing.py
from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path('ws/intermediate_results/', consumers.IntermediateResultConsumer.as_asgi()),
]
