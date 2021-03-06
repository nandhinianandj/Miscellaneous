#! /usr/bin/env python

from scapy.all import *
ap_list =[]

def PacketHandler(pkt):
    if pkt.haslayer(Dot11):
        if pkt.type==0 and pkt.subtype==8:
            if pkt.addr2 not in ap_list:
                ap_list.append(pkt.addr2)
                print "AP MAC: %s with SSID : %s" %(pkt.addr2,pkt.info)

def raw_socket_ssid_sniffer():
	import socket
	rawSocket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.htons(0x0003))
	rawSocket.bind(("mon0", 0x0003))
	ap_list = set()
	while True :
		pkt = rawSocket.recvfrom(2048)[0]
		if pkt[26] == "\x80" :
			if pkt[36:42] not in ap_list  and ord(pkt[63]) > 0:
				ap_list.add(pkt[36:42])
				print "SSID: %s  AP MAC: %s" % (pkt[64:64 +ord(pkt[63])], pkt[36:42].encode('hex'))

sniff(iface="mon0",prn=PacketHandler)

#raw_socket_ssid_sniffer()
