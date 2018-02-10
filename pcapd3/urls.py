from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pcap.urls')),
    path('pcap/', include('pcap.urls')),
    path('admin/', admin.site.urls),
]
