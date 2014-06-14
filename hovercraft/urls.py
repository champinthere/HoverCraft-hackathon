from django.conf.urls import patterns, include, url
from django.shortcuts import render
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

# from django.http import HttpResponse

admin.autodiscover()

def index(request):
    return render(request, 'index.html')


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hovercraft.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include('login.urls', namespace="login")),
    url(r'^$', index),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


