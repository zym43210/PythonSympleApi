from django.db import models
from authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, default=None)
