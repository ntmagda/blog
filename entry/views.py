from django.shortcuts import render

from django.views import generic
# Create your views here.
from . import models

class EntryView(generic.DetailView):
    template_name = "entry/EntryDetails.html"
    model = models.Entry

    def get_context_data(self, **kwargs):
        context = super(EntryView, self).get_context_data(**kwargs)
        return context