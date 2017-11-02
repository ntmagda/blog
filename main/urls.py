from django.conf.urls import url, include
from . import views as MainViews


app_name = 'main'
urlpatterns = [
    url(r'^contact/$', MainViews.ContactView.as_view(), name='contact'),
    url(r'^aboutus/$', MainViews.AboutUsView.as_view(), name='aboutus'),
    url(r'^articles/', include('entry.urls', namespace="entry")),
    url(r'^$', MainViews.Index.as_view(), name='home'),
]
