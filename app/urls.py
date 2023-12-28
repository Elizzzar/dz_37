from django.urls import path
from .views import *

urlpatterns = [
    path('', ListBooks.as_view(), name='list_books'),
    path('create_book/', CreateBook.as_view(), name='create_book'),
    path('book/<int:id>', DetailBook.as_view(), name='detail_book'),
    path('update_book/<int:id>', UpdataBook.as_view(), name='update_book'),
    path('delete_book/<int:id>', DeleteBook.as_view(), name='delete_book'),
]
