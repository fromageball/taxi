from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.core.urlresolvers import reverse
from blog.feed import RSSFeed
from django.views.generic.dates import YearArchiveView
from blog.views import BlogYearArchiveView, BlogMonthArchiveView
from django.conf import settings


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^$', 'blog.views.index', name='index'),
    url(r'^about/$', 'blog.views.about', name='about'),
    url(r'^contact/$', 'blog.views.contact', name='contact'),
    url(r'^single/(?P<slug>[\w-]+)/$', 'blog.views.single', name='single'),
    url(r'^archive/$', 'blog.views.archive', name="archive"),
    url(r'^archive/(?P<year>\d{4})/$', BlogYearArchiveView.as_view(), name="archiveYear"),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{1,2})/$', BlogMonthArchiveView.as_view(month_format='%m'), name="archiveMonth"),
    url(r'^theindustry/$', 'blog.views.theindustry', name='theindustry'),
    url(r'^rss/$', RSSFeed()),
    url(r'^search/', 'blog.views.search', name='search'),
    url(r'^comments/', include('django.contrib.comments.urls')),
    
    # url(r'^newblog/', include('newblog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    
    
) 

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))


