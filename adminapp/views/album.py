from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from adminapp.forms import AlbumEditForm, PhotoEditForm
from mane.models import Album, Photo


class AlbumListView(ListView):
    model = Album
    template_name = 'adminapp/album_list.html'


class AlbumUpdateView(UpdateView):
    model = Album
    template_name = 'adminapp/album_form.html'
    form_class = AlbumEditForm
    success_url = reverse_lazy('adminapp:album_list')


class AlbumDeleteView(DeleteView):
    model = Album
    template_name = 'adminapp/album_delete_confirm.html'
    success_url = reverse_lazy('adminapp:album_list')


class PhotoListView(ListView):
    model = Photo
    template_name = 'adminapp/photo_list.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data()
        context_data['album_pk'] = self.kwargs['album_pk']
        return context_data


    def get_queryset(self):
        return super().get_queryset().filter(album__pk=self.kwargs['album_pk'])

class AlbumCreateView (CreateView):
    model = Album
    template_name = 'adminapp/album_form.html'
    form_class = AlbumEditForm
    success_url = reverse_lazy('adminapp:album_list')

class AlbumReadView (DetailView):
    model = Album
    template_name = 'adminapp/album_read.html'




