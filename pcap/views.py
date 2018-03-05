from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Pcap
from .forms import UploadForm
from django.http import HttpResponseRedirect, HttpResponse
from.parser import tsharkpcap


def upload(request):
    form = UploadForm(request.POST or None, request.FILES or None)
    uploadpcap = UploadForm()
    if form.is_valid():
        form.save()
        file = request.FILES['pcap_file']
        filename = str(file)
        # handle uploaded file
        tsharkpcap(file, filename)
        return HttpResponseRedirect('/visualize')
    return render(request, 'pcap/pcap_form.html', {'form': uploadpcap})

def visualizepcap(request):
    return HttpResponse('Hello there sweety')

class IndexView(generic.ListView):
    template_name = 'pcap/index.html'
    context_object_name = 'pcaps'

    def get_queryset(self):
        return Pcap.objects.all()

# not using this class atm
class AddPcap(CreateView):
    model = Pcap
    fields = ['pcap_file']




