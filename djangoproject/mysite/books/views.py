#DjangoProject/books/views.py
from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Book, Author, Publisher

#Template View
class BooksModelView(TemplateView):
    template_name = 'books/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_list'] = ['Book','Author','Publisher']
        return context

class BookList(ListView):
    model = Book

class AuthorList(ListView):
    model = Publisher

class PublisherList(ListView):
    model = Publisher

class BookDetail(DetailView):
    model = Book

class AuthorDetail(DetailView):
    model = Author

class PublisherDetail(DetailView):
    model = Publisher