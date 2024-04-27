# -*- coding: utf-8 -*-
"""
ASGI config for news_articles project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

# import os

# from django.core.asgi import get_asgi_application
# from django.core.handlers.asgi import ASGIHandler

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_articles.settings")

# application: ASGIHandler = get_asgi_application()


# # news_articles/asgi.py

# # news_articles/asgi.py
# import os
# from django.core.asgi import get_asgi_application
# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter
# # import news.routing

# from news import routing

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_articles.settings")

# application = ProtocolTypeRouter(
#     {
#         "http": get_asgi_application(),
#         "websocket": AuthMiddlewareStack(
#             URLRouter(routing.websocket_urlpatterns)
#         ),
#     }
# )

# news_articles/asgi.py
import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import news.routing

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "news_articles.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),  # Django's ASGI application to handle traditional HTTP requests
        "websocket": AuthMiddlewareStack(
            URLRouter(
                news.routing.websocket_urlpatterns  # Directing WebSocket traffic to your app's routing configuration
            )
        ),
    }
)
