from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('upload/', views.AddPcap.as_view(), name='upload'),
    path('upload/', views.upload, name='upload'),
    path('sankey/', views.sankey, name='sankey'),
    path('sankey-udp/', views.sankeyudp, name='sankeyudp'),
    path('table-tcp/', views.tabletcp, name='tabletcp'),
    path('table-udp/', views.tableucp, name='tableucp'),
]
