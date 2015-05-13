from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^add/$', 'authors.views.add', name='authors_add'),
)