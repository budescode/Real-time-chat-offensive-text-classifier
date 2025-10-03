from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from django.urls import path
from chat import consumers  
from django.core.asgi import get_asgi_application

application = ProtocolTypeRouter({
    "http": get_asgi_application(),  # Django views
    "websocket": AuthMiddlewareStack(
        URLRouter([
            path("ws/chat/<str:username>/", consumers.ChatConsumer.as_asgi()),
        ])
    ),
})
