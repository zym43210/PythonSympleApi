from django.urls import path

from books.api.v1.views import (
    BooksListView)

app_name = 'books'
urlpatterns = [

    path('', BooksListView.as_view()),
    path('<int:id>', BooksListView.as_view()),
]
