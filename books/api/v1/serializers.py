from abc import ABC

from rest_framework import serializers
from books.models import Book
from authors.models import Author


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['title', 'description', 'author_name']

    def create(self, validated_data):
        name = validated_data['author_name']
        validated_data['author_name'] = Author.objects.get(name=name)
        print(validated_data['author_name'])
        return Book.objects.create(**validated_data)
