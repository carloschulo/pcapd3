from django.db import models

# Create your models here.

class Pcap(models.Model):
    pcap_file = models.FileField()