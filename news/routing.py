# -*- coding: utf-8 -*-
# news/routing.py
from django.urls import re_path
from .consumers import NewsConsumer

websocket_urlpatterns = [
    re_path(r"^ws/news/(?P<news_id>\d+)/$", NewsConsumer.as_asgi()),
]
