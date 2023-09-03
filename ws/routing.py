from django.urls import re_path
from ws.consumers import WSConsumer

channel_routing = [
    re_path("connect", WSConsumer.as_asgi())
]
