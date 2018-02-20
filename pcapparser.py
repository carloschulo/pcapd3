#!/usr/bin/env python

import os, subprocess, csv, operator, re

# argu = "tshark -r sample.pcap -T fields -E separator=, -E quote=d -e tcp.dstport -e ip.addr -e tcp.stream | sort | uniq | sort > output.csv"
#
# os.system(argu)
# returns = os.system("tshark -r sample.pcap -T fields -E separator=, -E quote=d -e tcp.dstport -e ip.addr -e tcp.stream | sort | uniq | sort")

# print()
#
# inpu = "tshark -r sample.pcap -T fields -e frame.number -e tcp.dstport -e ip.addr -e tcp.stream -l"
# p = subprocess.Popen(inpu, stdout=subprocess.PIPE, shell=True)

# print(p.stdout.readline())
#
# for frame in iter(p.stdout.readline):
#     print(frame)

# tshark = "tshark -r sample.pcap -T fields -e frame.number -e tcp.dstport -e ip.addr -e tcp.stream > out.txt"
# os.system(tshark)
# tcsv = "tshark -r sample.pcap -T fields -e tcp.stream  -e frame.number -e tcp.dstport -e ip.addr -E separator=, > out.csv"
# os.system(tcsv)
#
# with open('out.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     sort = sorted(csv_reader, key=lambda x: int(x[0]))
#     for line in sort:
#         print(line)


x = []
dic = {}
def handlelist(index, input):
    x.append(input[0])
    print(index, input)


def handlefile():
    filepath = "tezt.txt"
    with open(filepath) as f:
        for index, line in enumerate(f):
            packet = line.splitlines()
            newpacket = re.split(r'\t+', packet[0].rstrip('\t'))
            handlelist(index, newpacket)


handlefile()
# print(x)

