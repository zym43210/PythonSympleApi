from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=50, null=False, blank=True)
    author_name = models.TextField(max_length=50, null=False, blank=True)
    description = models.TextField(max_length=500, null=False, blank=True)
