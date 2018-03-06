import os, csv, pandas as pd


def tsharkpcap(pcapfile, filename):
    name = filename.split('.')
    name[0] = 'pcap'
    tcp_outputtxtname = f'tcp-{name[0]}.txt'
    udp_outputtxtname = f'udp-{name[0]}.txt'

    # used for sankey
    tcpconv_txtname = f'tcpconv-{name[0]}.txt'
    udpconv_txtname = f'udpconv-{name[0]}.txt'
    tcptshark = f'tshark -n -r {pcapfile} -T fields -E header=y -e tcp.stream -e ip.src -e tcp.srcport -e ip.dst -e tcp.dstport -e frame.protocols | sort -un | grep -a "tcp"> pcap/tsharkout/{tcp_outputtxtname}'
    udptshark = f'tshark -n -r sample.pcap -T fields -E header=y -e frame.number -e ip.src -e udp.srcport -e ip.dst -e udp.dstport -e frame.protocols -e ip.proto | grep -a "udp" > pcap/tsharkout/{udp_outputtxtname}'

    tcpconv = f'tshark -r {pcapfile} -qz conv,tcp | grep -v "================================================================================" | grep -v "TCP Conversations" | grep -v "Filter:<No Filter>" | grep -v "|       <-      | |       ->      | |     Total     |    Relative    |   Duration   |" | grep -v "| Frames  Bytes | | Frames  Bytes | | Frames  Bytes |      Start     |              |" > pcap/tsharkout/{tcpconv_txtname}'
    udpconv = f'tshark -r {pcapfile} -qz conv,udp | grep -v "================================================================================" | grep -v "UDP Conversations" | grep -v "Filter:<No Filter>" | grep -v "|       <-      | |       ->      | |     Total     |    Relative    |   Duration   |" | grep -v "| Frames  Bytes | | Frames  Bytes | | Frames  Bytes |      Start     |              |" > pcap/tsharkout/{udpconv_txtname}'
    os.system(tcptshark)
    os.system(udptshark)
    os.system(tcpconv)
    os.system(udpconv)

    tcp_outfile = f'pcap/tsharkout/{tcp_outputtxtname}'
    udp_outfile = f'pcap/tsharkout/{udp_outputtxtname}'

    tcpconv_outfile = f'pcap/tsharkout/{tcpconv_txtname}'
    udpconv_outfile = f'pcap/tsharkout/{udpconv_txtname}'

    tcp_len = convparser(tcpconv_outfile, 'tcp')
    udp_len = convparser(udpconv_outfile, 'udp')

    parsepcap(tcp_outfile, name[0], 'tcp')
    parsepcap(udp_outfile, name[0], 'udp')

    return {"tcp_len": tcp_len, "udp_len": udp_len}


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


def convparser(txt_file, proto):
    with open(txt_file, 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        # remove arrows
        removearr = (line.replace('<->', '') for line in stripped if line)
        # strip ports from IP address
        # getports = (line.replace(':', ' ') for line in removearr if line)
        lines = (line.split() for line in removearr if line)
        with open(f'pcap/csvfiles/{proto}-init-sankey.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('Address A', 'Address B', 'Packet B to A Frames', 'Packet B to A Bytes',
                             'Packet A to B Frames', 'Packet A to B Bytes', 'Total Packet', 'Total Bytes',
                             'Relative Start', 'Duration'))
            for line in lines:
                writer.writerow(line)

    df = pd.read_csv(f'pcap/csvfiles/{proto}-init-sankey.csv')
    df.sort_values(["Relative Start"], inplace=True, ascending=True)
    df['Total Packet'] = round(df['Total Packet'] * .1, 5)
    df.drop(
        ['Packet B to A Frames', 'Packet B to A Bytes', 'Packet A to B Frames', 'Packet A to B Bytes', 'Total Bytes',
         'Relative Start', 'Duration'], axis=1, inplace=True)
    df.rename(columns={'Address A': 'source', 'Address B': 'target', 'Total Packet': 'value'}, inplace=True)
    df.to_csv(f'pcap/csvfiles/{proto}-sankey.csv', index=False)
    return len(df.index)
