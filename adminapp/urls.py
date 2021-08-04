from django.urls import path

from adminapp import views as admin_views

app_name = 'adminapp'

urlpatterns = [
    path('', admin_views.news_list, name='news_list'),
    path('update/<int:pk>/', admin_views.news_update, name='news_update'),
    path('create/', admin_views.news_create, name='news_create'),
    path('delete/<int:pk>/', admin_views.news_delete, name='news_delete'),
]
