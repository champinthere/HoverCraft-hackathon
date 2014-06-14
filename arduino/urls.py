from django.conf.urls import patterns, url
from django.contrib import admin


# from django.http import HttpResponse

admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hovercraft.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^control', 'arduino.views.control', name='control'),
    url(r'^manage', 'arduino.views.manage', name='manage'),
)