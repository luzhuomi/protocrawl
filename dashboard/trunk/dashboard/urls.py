import os
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        (r'^$', 'main.views.home_redirect'),
        (r'^main/$', 'main.views.home'),
        (r'main/', include('gmapi.urls.media')),        
        (r'main/tweet/(?P<page_index>\d+)/(?P<page_size>\d+)/', 'main.views.tweet_ajax'),
        (r'main/tweet/total/(?P<page_size>\d+)/', 'main.views.tweet_total_ajax'),        
        (r'main/mood/(?P<age_band>.+)/(?P<gender>.+)/(?P<race>.+)/(?P<mood>.+)/', 'main.views.mood_ajax'),
        (r'main/profile/(?P<age_band>.+)/(?P<gender>.+)/(?P<race>.+)/(?P<mood>.+)/(?P<dimension>.+)/', 'main.views.profile_ajax'),                
        (r'main/map/$', 'main.views.map'),
        (r'main/map/', include('gmapi.urls.media')), # for debug
        (r'^static_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.APP_DIR, 'static_media/')}),
    # Examples:
    # url(r'^$', 'dashboard.views.home', name='home'),
    # url(r'^dashboard/', include('dashboard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
