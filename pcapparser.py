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
newDic = {}

def handlelist(index, input):
    if input[0] != '':
        # if index ==
        x.append(input)
        # dic[index] = input

        # print(index, input)
    else:
        return


def handlefile():
    filepath = "tezt.txt"
    with open(filepath) as f:
        for index, line in enumerate(f):
            packet = line.splitlines()
            newpacket = re.split(r'\t+', packet[0].rstrip('\t'))
            handlelist(index, newpacket)


# def splitlist(ls):
#     listlen = ls.__len__()
#     for elem in ls:
#         if elem[0] ==
#     print(ls)


# handlefile()
# splitlist(x)
# print(x)

with open('tcp-conv.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    # remove arrows
    removearr = (line.replace('<->', '') for line in stripped if line)
    lines = (line.split() for line in removearr if line)
    with open('tcp-conv.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Address A', 'Address B', 'Packet B to A Frames', 'Packet B to A Bytes', 'Packet A to B Frames', 'Packet A to B Bytes', 'Total Packet', 'Total Bytes', 'Relative Start', 'Duration'))
        for line in lines:
            writer.writerow(line)

