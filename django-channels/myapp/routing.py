from django.urls import path
from . import consumers

websocket_url_patterns = [
    path('ws/app/', consumers.TesteConsumer.as_asgi())
]