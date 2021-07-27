from django.shortcuts import render

import news
from news.models import News, Category


def news_list_all(request):
    # все новости
    context = {
        'news': News.objects.all()
    }
    return render(request, 'news/news.html', context)


def news_list(request, pk):
    # новости по категории
    items = News.objects.filter(category__pk=pk)
    context = {
        'items': items,
    }
    return render(request, 'news/news.html', context)


def news_item(request, pk):
    # отдельная новость
    item = News.objects.get(pk=pk)
    context = {
        'item': item,
        'categoris': Category.objects.all()
    }
    return render(request, 'news/news_item.html', context)
