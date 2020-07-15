from django.urls import path

from books.api.v1.views import (
    BooksView,
    FindBook,
    BooksListView)

app_name = 'books'
urlpatterns = [
    # path('', BooksView.as_view()),
    # path('<id>', FindBook.as_view()),
    path('', BooksListView.as_view()),
    path('<int:id>', BooksListView.as_view()),
]
