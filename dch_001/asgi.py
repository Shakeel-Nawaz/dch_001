import os

from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
from django.urls import path
from app1.consumers import TestConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
ws_patterns = [
    path('ws/test/',TestConsumer.as_asgi())
]
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    'websocket':URLRouter(ws_patterns)
    # Just HTTP for now. (We can add other protocols later.)
})
