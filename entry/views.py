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
    paginate_by = 5

    def get_queryset(self):
        queryset = models.Entry.objects.published()
        if len(self.kwargs) > 0:
            if 'slug_country' in self.kwargs:
                queryset = queryset.filter(country__slug=self.kwargs['slug_country'])
            if 'slug_tag' in self.kwargs:
                queryset = queryset.filter(tags__name__in=[self.kwargs['slug_tag']])
        return queryset

    def get_context_data(self, **kwargs):
        context = super(EntryListView, self).get_context_data(**kwargs)
        tags = Tag.objects.all()
        context['tag_list'] = tags
        return context

class ClimbingView(generic.ListView):
    template_name = "entry/EntryList.html"
    paginate_by = 5

    queryset = models.Entry.objects.published().filter(isClimbing=True)