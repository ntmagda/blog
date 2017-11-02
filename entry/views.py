from django.shortcuts import render

from django.views import generic
# Create your views here.
from . import models
from taggit.models import Tag
from django.views.generic.base import ContextMixin
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext

class BaseContextMixin(ContextMixin):

    def get_context_data(self, **kwargs):
        context_data = super(BaseContextMixin, self).get_context_data(**kwargs)
        return context_data

class EntryView(generic.DetailView):
    template_name = "entry/EntryDetails.html"
    model = models.Entry

    def get_context_data(self, **kwargs):
        context = super(EntryView, self).get_context_data(**kwargs)
        return context

class EntryTipFullArticleView(generic.DetailView):
    template_name = "entry/EntryTip.html"
    model = models.EntryTipFullArticle

    def get_context_data(self, **kwargs):
        context = super(EntryTipFullArticleView, self).get_context_data(**kwargs)
        return context


class EntryListView(generic.ListView):
    template_name = "entry/EntryList.html"

    def get_queryset(self):
        if len(self.kwargs)> 0:
            queryset = models.Entry.objects.published().filter(tags__name__in=[self.kwargs['slug']])
        else:
            queryset = models.Entry.objects.published()
        return queryset

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tag_list'] = tags
        return context