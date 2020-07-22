from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=30, unique=True)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

    def __str__(self):
        return '%s' % self.name
