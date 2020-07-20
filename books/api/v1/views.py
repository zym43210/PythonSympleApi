from rest_framework import generics
from rest_framework import mixins

import django_filters.rest_framework
from books.models import Book
from books.api.v1.serializers import BookSerializer


class BooksListView(generics.GenericAPIView,
                    mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['title', 'author_name']

    lookup_field = 'id'

    def get(self, request, id=None):
        if id:
            return self.retrieve(request, id)
        else:
            return self.list(request)

    def post(self, request):

        return self.create(request)
