import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render

from mane.models import Album, Photo


def main(request):
    context = {
        'albums': Album.objects.all()
    }
    return render(request, 'mane/index.html', context)


def albums(request):
    context = {
        'albums': Album.objects.all()
    }
    return render(request, 'mane/index.html', context) #album templates


def photo(request, pk):
    current_photo = Photo.objects.get(pk=pk)
    context = {
        'title': '123213',
        'photo': current_photo
    }
    return render(request, 'mane/photo.html', context)


def album(request, pk):
    album_item = Album.objects.get(pk=pk)
    photos = Photo.objects.filter(album__pk=pk)
    context = {
        'title': 'Альбом с фотографиями',
        'album': album_item,
        'photos': photos
    }
    return render(request, 'mane/album.html', context)

def photo_like(request, pk):
    photo_item = Photo.objects.get(pk=pk)
    photo_item.liked += 1
    photo_item.save()
    return HttpResponseRedirect(request.META['HTTP_REFERER'])

