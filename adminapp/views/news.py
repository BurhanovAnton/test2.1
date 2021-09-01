from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse_lazy
from adminapp.forms import NewEditForm
from news.models import News

from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import DetailView


class NewsListView(ListView):
    model = News
    template_name = 'adminapp/news_list.html'


class NewsUpdateView(UpdateView):
    model = News
    template_name = 'adminapp/news_form.html'
    form_class = NewEditForm
    success_url = reverse_lazy('adminapp:news_list')


def news_item(request):
    content = {
    }
    return render(request, 'adminapp/news_read.html', content)


class NewsCreateView(CreateView):
    model = News
    template_name = 'adminapp/news_form.html'
    form_class = NewEditForm
    success_url = reverse_lazy('adminapp:news_list')


# def news_delete(request, pk):
#     new_current_item = get_object_or_404(News, pk=pk)
#     if request.method == 'POST':
#         new_current_item.delete()
#         return HttpResponseRedirect(reverse('adminapp:news_list'))
#     content = {
#         'object': new_current_item
#     }
#     return render(request, 'adminapp/news_delete.html', content)

class NewsDeleteView(DeleteView):
    model = News
    template_name = 'adminapp/news_delete.html'
    success_url = reverse_lazy('adminapp:news_list')

class NewsReadView (DetailView):
    model = News
    template_name = 'adminapp/news_read.html'