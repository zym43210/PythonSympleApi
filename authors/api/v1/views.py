from django.db.models import Avg
from rest_framework import generics
from rest_framework import mixins

from authors.models import Author
from authors.api.v1.serializers import AuthorSerializer


class AuthorsListView(generics.GenericAPIView,
                      mixins.ListModelMixin,
                      mixins.CreateModelMixin):
    serializer_class = AuthorSerializer
    queryset = Author.objects.annotate(avg_price=Avg('books__price'))

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AuthorsDetailView(generics.GenericAPIView,
                        mixins.RetrieveModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.UpdateModelMixin):
    serializer_class = AuthorSerializer
    queryset = Author.objects.annotate(avg_price=Avg('books__price'))


    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
