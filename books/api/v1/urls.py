from django.urls import path

from books.api.v1.views import (
    BooksListView,
BooksDetailView)

app_name = 'books'
urlpatterns = [

    path('', BooksListView.as_view()),
    path('<int:id>', BooksDetailView.as_view()),
]
