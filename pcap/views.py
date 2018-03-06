from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Pcap
from .forms import UploadForm
from django.http import HttpResponseRedirect, HttpResponse
from.parser import tsharkpcap

length = {}
pcapfilename = ''
# upload view
def upload(request):
    form = UploadForm(request.POST or None, request.FILES or None)
    uploadpcap = UploadForm()
    if form.is_valid():
        form.save()
        file = request.FILES['pcap_file']
        filename = str(file)
        global pcapfilename
        pcapfilename = filename
        # handle uploaded file
        conv_len = tsharkpcap(file, filename)
        global length
        length = conv_len
        return HttpResponseRedirect('/')
    return render(request, 'pcap/pcap_form.html', {'form': uploadpcap})


def sankey(request):
    file_length = str(length["tcp_len"])
    print('TCP len is ' + file_length)
    return render(request, 'pcap/sankey.html', {'proto': 'tcp', 'file_length': file_length})


def sankeyudp(request):
    file_length = str(length["udp_len"])
    print('UDP len is ' + file_length)
    return render(request, 'pcap/sankey.html', {'proto': 'udp', 'file_length': file_length})


# Homepage
class IndexView(generic.ListView):
    template_name = 'pcap/index.html'
    context_object_name = 'pcaps'

    def get_queryset(self):
        name = str(Pcap.objects.last())
        return name

    def uploads(self):
        return Pcap.objects.all()


# not using this class view atm
class AddPcap(CreateView):
    model = Pcap
    fields = ['pcap_file']




