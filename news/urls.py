# -*- coding: utf-8 -*-
from django.urls import path
from django.urls.resolvers import URLPattern

from . import views

app_name: str = "news"
urlpatterns: list[URLPattern] = [
    # # ex: /news/
    # path(route="", view=views.IndexView.as_view(), name="index"),
    # # ex: /news/5/
    # path(
    #     route="<int:pk>/",
    #     view=views.DetailView.as_view(),
    #     name="detail",
    # ),
    # # ex: /news/5/results/
    # path(
    #     route="<int:pk>/results/",
    #     view=views.ResultsView.as_view(),
    #     name="results",
    # ),
    # # ex: /news/5/vote/
    # path(route="<int:question_id>/vote/", view=views.vote, name="vote"),
    path("home", views.news_homepage, name="index"),
    path("news/create/", views.create_news, name="news_create"),
    path("news/update/<int:news_id>/", views.update_news, name="news_update"),
    path("news/detail/<int:news_id>/", views.news_detail, name="news_detail"),
    path("news/delete/<int:news_id>/", views.news_delete, name="news_delete"),
    path(
        "search/", views.search_by_tags, name="search_by_tags"
    ),  # Make sure this is correct
]
