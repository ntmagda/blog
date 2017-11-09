from django.conf.urls import url, include
from . import views as MainViews
from entry import views as EntryView


app_name = 'main'
urlpatterns = [
    url(r'^climbing/$', EntryView.ClimbingView.as_view(), name='climbing'),
    url(r'^contact/$', MainViews.ContactView.as_view(), name='contact'),
    url(r'^countries/$', MainViews.CountriesView.as_view(), name='countries'),
    url(r'^aboutus/$', MainViews.AboutUsView.as_view(), name='aboutus'),
    url(r'^articles/', include('entry.urls', namespace="entry")),
    url(r'^$', MainViews.Index.as_view(), name='home'),
]
