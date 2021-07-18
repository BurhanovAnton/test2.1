from django.urls import path

from mane import views as mane_views

app_name = 'album'

urlpatterns = [
    path('photo/<pk>/', mane_views.photo, name='photo'),
    path('<pk>/', mane_views.album, name='album')
]

