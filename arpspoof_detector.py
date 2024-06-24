#!/usr/bin/env python3 
import scapy.all as scapy
import netifaces
def detect():
    print("\n****************************************************************")
    print("\n* Copyright of saai jeshwanth && nithesh, 2021 *")
    print("\n****************************************************************")
    def scan(ip):
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
        return answered_list[0][1].hwsrc
    def sniff(interface):
        scapy.sniff(iface=interface, store=False, prn=sniffed_packet)
    
    def sniffed_packet(packet):
        if packet.haslayer(scapy.ARP) and packet[scapy.ARP].op == 2:
            try:
                real_mac = scan(packet[scapy.ARP].psrc)
                response_mac = packet[scapy.ARP].hwsrc
                if real_mac != response_mac: 
                    print("[+] YOUR UNDER ATTACK")
            except IndexError:
                pass       
        
    sniff("wlan0")