from django.urls import path

from adminapp import views as admin_views

app_name = 'adminapp'

urlpatterns = [
    path('', admin_views.NewsListView.as_view(), name='news_list'),
    path('update/<pk>/', admin_views.NewsUpdateView.as_view(), name='news_update'),
    path('create/', admin_views.NewsCreateView.as_view(), name='news_create'),
    path('delete/<pk>/', admin_views.NewsDeleteView.as_view(), name='news_delete'),
    path('read/<pk>/', admin_views.NewsReadView.as_view(), name='news_read'),

    path('albums/', admin_views.AlbumListView.as_view(), name='album_list'),
    path('albums/<pk>/update/', admin_views.AlbumUpdateView.as_view(), name='album_update'),
    path('albums/<album_pk>/photos/', admin_views.PhotoListView.as_view(), name='album_photo_list'),
    path('albums/<pk>/delete/', admin_views.AlbumDeleteView.as_view(), name='album_delete'),
    path('albums/create/', admin_views.AlbumCreateView.as_view(), name='album_create'),
    path('albums/<pk>/read/', admin_views.AlbumReadView.as_view(), name='album_read'),

    path('photos/<album_pk>/create/', admin_views.PhotoCreateView.as_view(), name='photo_create'),
    path('photo/<pk>/update/', admin_views.PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<pk>/delete/', admin_views.PhotoDeleteView.as_view(), name='photo_delete'),
    path('photo/<pk>/read/', admin_views.PhotoReadView.as_view(), name='photo_read'),

]
