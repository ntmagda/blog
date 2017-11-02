from django.contrib import admin
from django.contrib import admin

from .models import Entry, EntryImage, EntryTipFullArticle, EntrySmallTip, AboutUsImage, AboutUs


class EntryImageInline(admin.TabularInline):
    model = EntryImage
    extra = 3

class EntryTipInline(admin.TabularInline):
    model = EntrySmallTip
    extra = 3

class AboutUsImageInline(admin.TabularInline):
    model = AboutUsImage
    extra = 3

class EntryAdmin(admin.ModelAdmin):
    inlines = [EntryImageInline, EntryTipInline, ]
    list_display = ['title', 'short_body','slug','get_tags']

    def get_tags(self, entry):
        tags = []
        for tag in entry.tags.all():
            tags.append(str(tag))
        return ', '.join(tags)


class EntryTipFullArticleAdmin(admin.ModelAdmin):
    model = EntryTipFullArticle
    list_display = ['title', 'short_body', 'slug', 'get_tags']

    def get_tags(self, entry):
        tags = []
        for tag in entry.tags.all():
            tags.append(str(tag))
        return ', '.join(tags)

class AboutUsAdmin(admin.ModelAdmin):
    inlines = [AboutUsImageInline, ]
    list_display = ['title','leon_image','magda_image']


admin.site.register(EntryTipFullArticle, EntryTipFullArticleAdmin)
admin.site.register(Entry, EntryAdmin)
admin.site.register(AboutUs, AboutUsAdmin)