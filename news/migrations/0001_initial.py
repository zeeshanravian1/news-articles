# -*- coding: utf-8 -*-
# Generated by Django 5.0.4 on 2024-04-25 13:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Tag",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=200)),
                ("text", models.TextField()),
                (
                    "image",
                    models.ImageField(
                        blank=True, null=True, upload_to="news_images"
                    ),
                ),
                ("likes", models.IntegerField(default=0)),
                ("dislikes", models.IntegerField(default=0)),
                (
                    "tags",
                    models.ManyToManyField(
                        blank=True, null=True, to="news.tag"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="NewsTags",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "news",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="news.news",
                    ),
                ),
                (
                    "tag",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="news.tag",
                    ),
                ),
            ],
            options={
                "unique_together": {("news", "tag")},
            },
        ),
    ]
