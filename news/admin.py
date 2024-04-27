# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import News, NewsTags, Tag

admin.site.register(Tag)
admin.site.register(News)
admin.site.register(NewsTags)
