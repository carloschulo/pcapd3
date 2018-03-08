#!/usr/bin/env python

import os, subprocess, csv, operator, re, pandas as pd

with open('udp-sankey.txt', 'r') as in_file:
    stripped = (line.strip() for line in in_file)
    # remove arrows
    removearr = (line.replace('<->', '') for line in stripped if line)
    # strip ports from IP address
    # getports = (line.replace(':', ' ') for line in removearr if line)
    lines = (line.split() for line in removearr if line)
    with open('udp-sankey.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Address A', 'Address B', 'Packet B to A Frames', 'Packet B to A Bytes', 'Packet A to B Frames', 'Packet A to B Bytes', 'Total Packet', 'Total Bytes', 'Relative Start', 'Duration'))
        for line in lines:
            writer.writerow(line)

df = pd.read_csv('udp-sankey.csv')
length = len(df.index)
# print('length is ' + str(length))
df.sort_values(["Relative Start"], inplace=True, ascending=True)
df['Total Packet'] = round(df['Total Packet'] * .1, 5)
df.drop(['Packet B to A Frames', 'Packet B to A Bytes', 'Packet A to B Frames', 'Packet A to B Bytes', 'Total Bytes', 'Relative Start', 'Duration'], axis=1, inplace=True)
df.rename(columns={'Address A': 'source', 'Address B': 'target', 'Total Packet': 'value'}, inplace=True)
df.to_csv('new-udp.csv', index=False)
