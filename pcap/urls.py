from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # path('upload/', views.AddPcap.as_view(), name='upload'),
    path('upload/', views.upload, name='upload'),
    path('visualize/', views.visualizepcap, name='visualizer'),
]
