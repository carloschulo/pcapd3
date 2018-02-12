from django.db import models
from django.urls import reverse

# Create your models here.


class Pcap(models.Model):
    pcap_file = models.FileField()
    # print(pcap_file)

    def __str__(self):
        return self.pcap_file.name

    def get_absolute_url(self):
        return reverse('index')
