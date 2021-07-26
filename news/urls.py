from django.urls import path

from news import views as news_views

app_name = 'news'

urlpatterns = [
    path('news/', news_views.news_list, name='news_list'),
    path('news/<pk>/', news_views.news_item, name='news_item'),
]

