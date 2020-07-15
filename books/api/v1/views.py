
from rest_framework import status

from rest_framework.response import Response

from rest_framework.views import APIView

from books.models import Book
from books.api.v1.serializers import BookSerializer


class BooksList(APIView):
    def get(self, request):
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data)


class FindBook(APIView):
    def get(self, request, id):
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = BookSerializer(book)
        return Response(serializer.data)


class AddBook(APIView):
    def post(self,request):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
