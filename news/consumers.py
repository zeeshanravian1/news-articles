# -*- coding: utf-8 -*-
# news/consumers.py

import json

from channels.generic.websocket import AsyncWebsocketConsumer

from .models import News

import logging

logger = logging.getLogger(__name__)


class NewsConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        logger.debug("WebSocket connected")
        self.news_id = self.scope["url_route"]["kwargs"]["news_id"]
        await self.accept()

    async def disconnect(self, close_code):
        logger.debug("WebSocket disconnected")
        pass

    async def receive(self, text_data):
        logger.debug(f"Received data: {text_data}")
        text_data_json = json.loads(text_data)
        action = text_data_json["action"]

        news = News.objects.get(id=self.news_id)
        if action == "like":
            news.likes += 1
        elif action == "dislike":
            news.dislikes += 1
        news.save()

        await self.send(
            text_data=json.dumps(
                {"likes": news.likes, "dislikes": news.dislikes}
            )
        )
