from django.db import models
from django.utils import timezone

from authors.models import Author


class Book(models.Model):
    title = models.CharField(max_length=50, unique=True)
    description = models.TextField(max_length=500, blank=True)
    author_name = models.ForeignKey(Author, on_delete=models.CASCADE, default=None, related_name='books')
    price = models.IntegerField(default=0)
    pages_number = models.IntegerField(default=0)
    create_date = models.DateTimeField(blank=True, null=True)
    update_date = models.DateTimeField(blank=True, null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return '%s: %s' % (self.title, self.description)

    def save(self, *args, **kwargs):
        if not self.id:
            self.create_date = timezone.now()
        self.update_date = timezone.now()
        return super(Book, self).save(*args, **kwargs)