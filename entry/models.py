from __future__ import unicode_literals

from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from taggit.managers import TaggableManager


class EntryQuerySet(models.QuerySet):
    def published(self):
        return self.filter(publish=True)


class Entry(models.Model):
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=400)
    short_body = models.TextField()
    slug = models.SlugField(max_length=200, unique=True)
    tags = TaggableManager()
    publish = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    title_image = models.ImageField(upload_to='images/%Y/%m/%d', null=True)
    body = RichTextUploadingField()

    objects = EntryQuerySet.as_manager()

    class Meta:
        verbose_name_plural = "entries"

class EntryImage(models.Model):
    property = models.ForeignKey(Entry, related_name='images')
    image = models.ImageField(upload_to='images/%Y/%m/%d', null=True)
