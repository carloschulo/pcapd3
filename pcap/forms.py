from django import forms
from .models import Pcap

class UploadForm(forms.ModelForm):

    class Meta:
        model = Pcap
        fields = ['pcap_file']