from django.conf.urls import url, include
from . import views as EntryView


app_name = 'entry'

urlpatterns = [
    url(r'^$', EntryView.EntryListView.as_view(), name='articles'),
    url(r'^(?P<slug>[-\w]+)/$', EntryView.EntryView.as_view(), name='entry-detail'),
    url(r'^tips/(?P<slug>[-\w]+)/', EntryView.EntryTipFullArticleView.as_view(), name='entry-tip'),

]
