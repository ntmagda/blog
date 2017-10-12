from __future__ import unicode_literals

from django.db import models

from django.conf import settings


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Entry(models.Model):
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=400)
    author_img = models.ImageField(upload_to='author/', null=True)
    body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title_image = models.ImageField(upload_to='images/%Y/%m/%d', null=True)

    objects = EntryQuerySet.as_manager()