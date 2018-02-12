from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Pcap

from django.http import HttpResponse


class IndexView(generic.ListView, ):
    template_name = 'pcap/index.html'
    context_object_name = 'pcaps'

    def get_queryset(self):
        return Pcap.objects.all()


class AddPcap(CreateView):
    model = Pcap
    fields = ['pcap_file']

