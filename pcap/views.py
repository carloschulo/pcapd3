from django.shortcuts import render


from django.http import HttpResponse


def index(request):
    # return HttpResponse("Upload PCAP.")
    return render(request, 'pcap/index.html')
