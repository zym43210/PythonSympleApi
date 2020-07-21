from rest_framework import serializers

from books.models import Book


class BookSerializer(serializers.ModelSerializer):
    # author_name = serializers.StringRelatedField(source='author_name.name', read_only=True)

    class Meta:
        model = Book
        fields = ['title', 'description', 'author_name']
