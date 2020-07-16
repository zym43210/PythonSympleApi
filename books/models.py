from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50)
    author_name = models.TextField(max_length=50)
    description = models.TextField(max_length=500, blank=True)
