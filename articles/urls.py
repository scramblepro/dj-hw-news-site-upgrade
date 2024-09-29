from django.urls import path

from articles.views import articles_list, article_detail

urlpatterns = [
    path('', articles_list, name='articles_list'),
    path('article/<slug:slug>/', article_detail, name='article_detail'),
]