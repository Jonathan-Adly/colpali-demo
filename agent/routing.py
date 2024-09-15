from django.urls import re_path

from . import consumers

websocket_urlpatterns = [
    re_path(
        r"^ws/llm-chat-websocket/(?P<chat_id>\w+)/?$",
        consumers.LLMWebsocketChatConsumer.as_asgi(),
    ),
]
