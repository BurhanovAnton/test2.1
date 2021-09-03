from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from adminapp.forms import CategoryEditForm

from news.models import Category


class CategoriesListView(ListView):
    model = Category
    template_name = 'adminapp/categories_list.html'


class CategoriesUpdateView(UpdateView):
    model = Category
    template_name = 'adminapp/categories_form.html'
    form_class = CategoryEditForm
    success_url = reverse_lazy('adminapp:categories_list')


class CategoriesCreateView(CreateView):
    model = Category
    template_name = 'adminapp/categories_form.html'
    form_class = CategoryEditForm
    success_url = reverse_lazy('adminapp:categories_list')


class CategoriesDeleteView(DeleteView):
    model = Category
    template_name = 'adminapp/categories_delete.html'
    success_url = reverse_lazy('adminapp:categories_list')
