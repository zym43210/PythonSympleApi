from django.urls import path

from books.api.v1.views import (
    BooksView,
    FindBook)

app_name = 'books'
urlpatterns = [
    path('', BooksView.as_view()),

    path('<id>', FindBook.as_view()),

]
