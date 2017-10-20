from django.contrib import admin
from django.contrib import admin

from .models import Entry, EntryImage


class EntryImageInline(admin.TabularInline):
    model = EntryImage
    extra = 3


class EntryAdmin(admin.ModelAdmin):
    inlines = [EntryImageInline, ]

admin.site.register(Entry, EntryAdmin)
