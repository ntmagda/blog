from django.contrib import admin
from django.contrib import admin

from .models import Entry, EntryImage


class EntryImageInline(admin.TabularInline):
    model = EntryImage
    extra = 3


class EntryAdmin(admin.ModelAdmin):
    inlines = [EntryImageInline, ]
    list_display = ['title', 'short_body','slug','get_tags']

    def get_tags(self, entry):
        tags = []
        for tag in entry.tags.all():
            tags.append(str(tag))
        return ', '.join(tags)


admin.site.register(Entry, EntryAdmin)
