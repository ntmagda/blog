from django.shortcuts import render

from django.views import generic
# Create your views here.
from . import models
from taggit.models import Tag
from django.views.generic.base import ContextMixin

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

class EntryListView(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "entry/EntryList.html"


    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tag_list'] = tags
        return context