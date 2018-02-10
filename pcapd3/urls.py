from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls import url
from django.views.static import serve

urlpatterns = [
    path('', include('pcap.urls')),
    path('pcap/', include('pcap.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'pcap_file/(?P<path>.*)$', serve,{
          'document_root': settings.MEDIA_ROOT,
        }),
    ]
