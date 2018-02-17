#!/usr/bin/env python

import os

# argu = "tshark -r sample.pcap -T fields -E separator=, -E quote=d -e tcp.dstport -e ip.addr -e tcp.stream | sort | uniq | sort > output.csv"
#
# os.system(argu)
returns = os.system("tshark -r sample.pcap -T fields -E separator=, -E quote=d -e tcp.dstport -e ip.addr -e tcp.stream | sort | uniq | sort")

# print()
