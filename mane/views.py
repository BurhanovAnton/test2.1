import datetime

from django.shortcuts import render

from mane.models import Album, Photo


def main(request):
    context = {
        'albums': Album.objects.all()
    }
    return render(request, 'mane/index.html', context)


def photo(request, pk):
    current_photo = {}
    albums = []
    for album_item in albums:
        if album_item['id'] == int(pk):
            current_photo = album_item
            break
    context = {
        'title': '123213',
        'photo': current_photo
    }
    return render(request, 'mane/photo.html', context)


def album(request,pk):
    album_item = Album.objects.get(pk=pk)
    photos = Photo.objects.filter(album__pk=pk)
    context = {
        'title': 'Альбом с фотографиями',
        'album': album_item,
        'photos': photos
    }
    return render(request, 'mane/album.html', context)