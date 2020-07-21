from django.db import models
from authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500, blank=True)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, related_name='books')

    def __unicode__(self):
        return self.title

    def __str__(self):
        return '%s: %s' % (self.title, self.description)
