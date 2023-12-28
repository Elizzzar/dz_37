from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from .models import Book
from .forms import BookForm
from django.urls import reverse_lazy

class ListBooks(ListView):
    model = Book
    template_name = 'list_books.html'
    context_object_name = 'books'

class CreateBook(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'create_book.html'
    success_url = reverse_lazy('list_books')

class DetailBook(DetailView):
    model = Book
    template_name = 'book.html'
    pk_url_kwarg = 'id'
    context_object_name = 'book'

class UpdataBook(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'update_book.html'
    pk_url_kwarg = 'id'
    context_object_name = 'book'
    success_url = reverse_lazy('list_books')

class DeleteBook(DeleteView):
    model = Book
    template_name = 'delete.html'
    pk_url_kwarg = 'id'
    success_url = reverse_lazy('list_books')