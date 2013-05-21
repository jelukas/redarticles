from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^(?P<article_id>\d+)/$', 'blog.views.single', name='single'),
)