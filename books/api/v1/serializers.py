from abc import ABC

from rest_framework import serializers
from books.models import Book


class BookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(required=True, max_length=50)
    author_name = serializers.CharField(required=True, max_length=50)
    description = serializers.CharField(required=True, max_length=500)

    def create(self, validated_data):

        return Book.objects.create(**validated_data)
