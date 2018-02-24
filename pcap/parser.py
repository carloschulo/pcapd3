import os, csv


def tsharkpcap(pcapfile, filename):
    name = filename.split('.')
    name[0] = 'pcap'
    tcp_outputtxtname = f'tcp-{name[0]}.txt'
    udp_outputtxtname = f'udp-{name[0]}.txt'
    tcptshark = f'tshark -n -r {pcapfile} -T fields -E header=y -e tcp.stream -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -e frame.protocols | sort -un | grep -a "tcp"> pcap/tsharkout/{tcp_outputtxtname}'
    udptshark = f'tshark -n -r sample.pcap -T fields -E header=y -e frame.number -e ip.src -e udp.srcport -e ip.dst -e udp.dstport -e frame.protocols -e ip.proto | grep -a "udp" > pcap/tsharkout/{udp_outputtxtname}'
    os.system(tcptshark)
    os.system(udptshark)
    tcp_outfile = f'pcap/tsharkout/{tcp_outputtxtname}'
    udp_outfile = f'pcap/tsharkout/{udp_outputtxtname}'
    parsepcap(tcp_outfile, name[0], 'tcp')
    parsepcap(udp_outfile, name[0], 'udp')


def parsepcap(txtfile, outputtxtname, proto):
    csvfile = f'pcap/csvfiles/{proto}-{outputtxtname}.csv'
    with open(txtfile, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split() for line in stripped if line)
        with open(csvfile, 'w') as out_file:
            writer = csv.writer(out_file)
            # writer.writerow(('tcp.stream', 'ip.src', 'tcp.srcport', 'ip.dst', 'tcp.dstport', 'frame.protocols'))
            for line in lines:
                writer.writerow(line)
