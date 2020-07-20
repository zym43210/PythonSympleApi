from abc import ABC

from rest_framework import serializers
from books.models import Book
from authors.models import Author


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=50)
    author_name = serializers.CharField(required=True, max_length=50)
    description = serializers.CharField(required=True, max_length=500)

    def create(self, validated_data):
        name = validated_data['author_name']
        validated_data['author_name'] = Author.objects.get(name=name)

        return Book.objects.create(**validated_data)
