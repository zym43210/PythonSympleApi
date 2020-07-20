from django.urls import path

from authors.api.v1.views import (
    AuthorsListView, AuthorsDetailView)

app_name = 'authors'
urlpatterns = [

    path('', AuthorsListView.as_view()),
    path('<int:pk>', AuthorsDetailView.as_view()),

]
