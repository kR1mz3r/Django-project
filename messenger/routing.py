from django.urls import path
from .consumer import ChatConsumer

websocket_urlpatterns = [
    path('ws/messenger/', ChatConsumer.as_asgi()),
]
http_urlpatterns = [
]
urlpatterns = websocket_urlpatterns + http_urlpatterns