import os
from django.conf import settings
from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
        (r'^$', 'main.views.home'),
        (r'', include('gmapi.urls.media')),        
        (r'tweet', 'main.views.tweet_ajax'),
        (r'mood/(?P<age_band>.+)/(?P<gender>.+)/(?P<race>.+)/', 'main.views.mood_ajax'),
        (r'profile/(?P<dimension>.+)/', 'main.views.profile_ajax'),                
        (r'^map/$', 'main.views.map'),
        (r'^map/', include('gmapi.urls.media')), # for debug
        (r'^static_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(settings.APP_DIR, 'static_media/')}),
    # Examples:
    # url(r'^$', 'dashboard.views.home', name='home'),
    # url(r'^dashboard/', include('dashboard.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
