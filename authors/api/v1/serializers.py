from django.db.models import Avg
from rest_framework import serializers
from authors.models import Author
from books.models import Book


class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.StringRelatedField(many=True)
    avg_price = serializers.FloatField(default=0)

    class Meta:
        model = Author
        fields = ['id', 'name', 'email', 'books', 'avg_price']
