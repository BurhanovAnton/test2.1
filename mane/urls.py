from django.urls import path

from mane import views as mane_views

app_name = 'album'

urlpatterns = [
    path('', mane_views.albums, name='albums'),
    path('photo/<pk>/', mane_views.photo, name='photo'),
    path('<pk>/', mane_views.album, name='album'),
    path('like/<pk>/', mane_views.photo_like, name='like_photo')
]

