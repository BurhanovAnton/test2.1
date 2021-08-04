from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from adminapp.forms import NewEditForm
from news.models import News


def news_list(request):
    content = {
    'object_list': News.objects.all()
    }
    return render(request, 'adminapp/news_list.html', content)


def news_item(request):
    content = {

    }
    return render(request, 'adminapp/news_item.html', content)


def news_create(request):
    if request.method == 'POST':
        news_form = NewEditForm(request.POST, request.FILES)
        if news_form.is_valid():
            news_form.save()
            return HttpResponseRedirect(reverse('adminapp:news_list'))
    else:
        news_form = NewEditForm()
    content = {
        'form': news_form
    }
    return render(request, 'adminapp/news_form.html', content)


def news_update(request, pk):
    new_current_item = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        news_form = NewEditForm(request.POST, request.FILES, instance=new_current_item)
        if news_form.is_valid():
            news_form.save()
            return HttpResponseRedirect(reverse('adminapp:news_list'))
    else:
        news_form = NewEditForm(instance=new_current_item)
    content = {
        'form': news_form
    }
    return render(request, 'adminapp/news_form.html', content)


def news_delete(request, pk):
    new_current_item = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        new_current_item.delete()
        return HttpResponseRedirect(reverse('adminapp:news_list'))

    content = {
        'object': new_current_item
    }
    return render(request, 'adminapp/news_delete.html', content)