from django.shortcuts import render, get_object_or_404

from articles.models import Article


def articles_list(request):
    template = 'articles/news.html'
    articles = Article.objects.order_by('-published_at')
    context = {
        'object_list': articles
    }

    return render(request, template, context)


def article_detail(request, slug):
    article = get_object_or_404(Article, slug=slug)
    template = 'articles/article_detail.html'
    context = {
        'article': article,
    }
    return render(request, template, context)
