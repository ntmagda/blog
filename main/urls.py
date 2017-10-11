from django.conf.urls import url
from . import views as MainViews
from entry.views import EntryView


app_name = 'main'
urlpatterns = [
    url(r'^contact/$', MainViews.ContactView.as_view(), name='contact'),
    url(r'^aboutus/$', MainViews.AboutUs.as_view(), name='aboutus'),
    url(r'^expeditions/$', MainViews.ExpeditionsView.as_view(), name='expeditions'),
    url(r'^expeditions/(?P<slug>[-\w]+)/$', EntryView.as_view(), name='entry-detail'),
    url(r'^$', MainViews.Index.as_view(), name='home'),
]
