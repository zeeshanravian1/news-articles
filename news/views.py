# -*- coding: utf-8 -*-
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import NewsForm
from .models import News, NewsTags, Tag


def news_homepage(request):
    news_list = News.objects.all()
    paginator = Paginator(news_list, 3)  # Show 3 news per page

    page = request.GET.get("page")
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)

    # Check for AJAX request
    if request.headers.get("X-Requested-With") == "XMLHttpRequest":
        return JsonResponse(
            {
                "news": list(news.object_list.values("id", "title", "text")),
                "has_next": news.has_next(),
            }
        )
    else:
        return render(request, "news/index.html", {"news": news})


def search_by_tags(request):
    query = request.GET.get("query", "")
    news_list = News.objects.none()
    if query:
        tag_names = query.split(",")
        tags = Tag.objects.filter(
            name__in=[name.strip() for name in tag_names]
        )
        news_list = News.objects.filter(newstags__tag__in=tags).distinct()
    return render(
        request, "news/search_results.html", {"news_list": news_list}
    )


def create_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            new_news = form.save(
                commit=False
            )  # Get the unsaved instance of News
            new_news.save()  # Save the news to get an ID

            # Process tags
            tags_input = request.POST.get("tags", "")

            tag_names = [
                tag.strip() for tag in tags_input.split(",") if tag.strip()
            ]
            for tag_name in tag_names:
                # Check if the tag already exists
                tag_instance, created = Tag.objects.get_or_create(
                    name=tag_name
                )
                # Associate the news with the tag
                NewsTags.objects.create(news=new_news, tag=tag_instance)

            return redirect("news:index")
    else:
        form = NewsForm()
    return render(request, "news/news_form.html", {"form": form})


# def news_detail(request, news_id):
#     # Retrieve the news article
#     news = get_object_or_404(News, pk=news_id)
#     return render(request, "news/post.html", {"news": news})


def news_detail(request, news_id):
    # Retrieve the news article along with its tags
    news = get_object_or_404(News, pk=news_id)
    tags = news.newstags_set.all()  # Assuming reverse lookup is newstags_set
    return render(request, "news/post.html", {"news": news, "tags": tags})


def update_news(request, news_id):
    news = News.objects.get(id=news_id)
    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            updated_news = form.save(
                commit=False
            )  # Get the unsaved instance of News
            updated_news.save()  # Save the news to get an ID

            # Process tags
            tags_input = request.POST.get("tags", "")

            tag_names = [
                tag.strip() for tag in tags_input.split(",") if tag.strip()
            ]
            for tag_name in tag_names:
                # Check if the tag already exists
                tag_instance, created = Tag.objects.get_or_create(
                    name=tag_name
                )
                # Associate the news with the tag
                NewsTags.objects.get_or_create(
                    news=updated_news, tag=tag_instance
                )

            return redirect("news:index")
    else:
        form = NewsForm(instance=news)
    return render(request, "news/news_form.html", {"form": form})


def news_delete(request, news_id):
    # delete news from news table also remove tags from NewsTags table
    news = News.objects.get(id=news_id)
    news.delete()
    return redirect("news:index")
