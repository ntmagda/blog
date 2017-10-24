from django.conf.urls import url
from . import views as MainViews
from entry import views as EntryView


app_name = 'main'
urlpatterns = [
    url(r'^contact/$', MainViews.ContactView.as_view(), name='contact'),
    url(r'^aboutus/$', MainViews.AboutUs.as_view(), name='aboutus'),
    url(r'^articles/$', EntryView.EntryListView.as_view(), name='articles'),
    url(r'^articles/(?P<slug>[-\w]+)/$', EntryView.EntryView.as_view(), name='entry-detail'),
    url(r'^$', MainViews.Index.as_view(), name='home'),
]
