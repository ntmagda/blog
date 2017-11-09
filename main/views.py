from django.views import generic
from django.utils import timezone
from entry.models import AboutUs
from entry import  models

class Index(generic.ListView):
    queryset = models.Entry.objects.published()
    template_name = "main/main_index.html"

class AboutUsView(generic.TemplateView):
    template_name = "main/aboutus.html"
    model = models.AboutUs

    def get_context_data(self, **kwargs):
        context = super(AboutUsView, self).get_context_data(**kwargs)
        context['object_list'] = AboutUs.objects
        return context

class ContactView(generic.TemplateView):
    template_name = "main/contact.html"


class CountriesView(generic.ListView):
    template_name = "main/grid.html"
    queryset = models.Country.objects.all()


