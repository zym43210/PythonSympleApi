from django.urls import path

from books.api.v1.views import (
    AddBook,
    BooksList,
    FindBook)

app_name = 'books'
urlpatterns = [
    path('all', BooksList.as_view()),
    path('add', AddBook.as_view()),
    path('<id>', FindBook.as_view()),

]
