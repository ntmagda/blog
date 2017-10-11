from django.views import generic
from django.utils import timezone
from entry import models


class Index(generic.TemplateView):
    template_name = "main/index.html"

class AboutUs(generic.TemplateView):
    template_name = "main/aboutus.html"

class ContactView(generic.TemplateView):
    template_name = "main/contact.html"

class ExpeditionsView(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "main/expeditions.html"
