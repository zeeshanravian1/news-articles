# news-articles

Monolithic Django application for managing news articles.
Implement a news list in Django with the ability to view news articles. Each news article should include tags. It should be possible to populate the news in the admin panel. Each news article consists of a Title, Text, Image, and tags.
There should be pages for: News, Single News Article, News by Tag.
There should also be a page for statistics on news views. (discuss later)

Django REST API for news articles.
Through a REST-API for news, there should be the ability to get/create/delete news articles.

Frontend in plain JavaScript.
Implement infinite scroll in plain JavaScript, which pulls 3 news articles at a time when scrolling without reloading the page. The idea of infinite scroll is to show data from the backend in pieces. Imagine that there are 1000 news articles in the database.

Statistics on news views.
Also, implement news article like and dislike in JavaScript, where liking a news article shows the current number of likes, even if another user of the site likes the article at the moment of viewing.


Design is not important, Bootstrap can be used.


Database Tables:

Tags:
- id
- name

python, ml

News:
- id
- title
- text
- image
- likes: int
- dislikes: int

deep learning
django

NewsTags:
- news_id
- tag_id
