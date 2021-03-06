from django.db import models
from django.urls import reverse


class Pcap(models.Model):
    pcap_file = models.FileField()

    def __str__(self):
        return self.pcap_file.name

    def get_absolute_url(self):
        return reverse('index')
