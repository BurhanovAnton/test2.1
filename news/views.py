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
    news_list_current = Category.objects.get(pk=pk)
    intro_news_item = News.objects.filter(news_list_current__pk=pk)# можно ли обратиться к другой модели? или создать данное поле в модели куатегорий?
    context = {
        'title': news_list_current,
        'intro': intro_news_item,
    }
    return render(request, 'news/news.html', context)


def news_item(request, pk):
    # отдельная новость
    item_title = News.objects.get(pk=pk)
    item_Body = News.objects.filter(item_title__pk=pk) # не уверен что строки 29,30,31 правильные
    item_Image = News.objects.filter(item_title__pk=pk)
    item_publish_at = News.objects.filter(item_title__pk=pk)

    context = {
        'title':item_title,
        'body': item_Body,
        'image': item_Image,
        'publish_at': item_publish_at,
    }
    return render(request, 'news/news.html', context)
