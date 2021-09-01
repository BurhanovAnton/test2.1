from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.urls import reverse
from adminapp.forms import PhotoEditForm
from mane.models import Photo


class PhotoCreateView(CreateView):
    model = Photo
    template_name = 'adminapp/photo_form.html'
    form_class = PhotoEditForm
    # success_url = reverse_lazy('adminapp:album_photo_list')

    def get_context_data(self, *, object_list=None, **kwargs):
        context_data = super().get_context_data()
        context_data['album_pk'] = self.kwargs['album_pk']
        return context_data

    def get_success_url(self):
        album_pk = self.kwargs.get('album_pk')
        return reverse('adminapp:album_photo_list', args=[album_pk])



class PhotoUpdateView(UpdateView):
    model = Photo
    template_name = 'adminapp/photo_form.html'
    form_class = PhotoEditForm
    # success_url = reverse_lazy('adminapp:album_photo_list')

    def get_success_url(self):
        photo_pk = self.kwargs.get('pk')
        album_pk = Photo.objects.get(pk=photo_pk).album.pk
        return reverse('adminapp:album_photo_list', args=[album_pk])


class PhotoDeleteView(DeleteView):
    model = Photo
    template_name = 'adminapp/photo_delete_confirm.html'
    # success_url = reverse_lazy('adminapp:album_photo_list')

    def get_success_url(self):
        photo_pk = self.kwargs.get('pk')
        album_pk = Photo.objects.get(pk=photo_pk).album.pk
        return reverse('adminapp:album_photo_list', args=[album_pk])


class PhotoReadView(DetailView):
    model = Photo
    template_name = 'adminapp/photo_read.html'