from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView
from .models import Pcap
from .forms import UploadForm
from django.urls import reverse


from django.http import HttpResponse

def upload(request):
    form = UploadForm(request.POST or None, request.FILES or None)
    uploadpcap = UploadForm()
    if form.is_valid():
        form.save()
        file = request.FILES['pcap_file']
        filename = str(file)
        print(filename)
        return HttpResponse('Success!')
    return render(request, 'pcap/pcap_form.html', {'form': uploadpcap})

class IndexView(generic.ListView):
    template_name = 'pcap/index.html'
    context_object_name = 'pcaps'

    def get_queryset(self):
        return Pcap.objects.all()


class AddPcap(CreateView):
    model = Pcap
    fields = ['pcap_file']
    # template_name = 'pcap/pcap_form.html'
    # success_url = 'pcap/'
    #
    # def post(self, request, *args, **kwargs):
    #     files = request.FILES.get('pcapupload')
    #     print('files', files)
    #     return render(request, 'pcap/success.html')



