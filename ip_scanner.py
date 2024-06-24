#!/usr/bin/env python3
import scapy.all as scapy
import argparse
import netifaces
def ip():
    print("\n****************************************************************")
    print("\n* Copyright of saai jeshwanth && nithesh, 2021 *")
    print("\n****************************************************************")
    


    def scan():
        gateways = netifaces.gateways()
        default_gateway = gateways['default'][netifaces.AF_INET][0]
        res=default_gateway+"/24" 
        #scapy.arping(res)
        print(res)
        ip = res
        arp_request = scapy.ARP(pdst=ip)
        broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
        arp_request_broadcast = broadcast/arp_request
        answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

        client_list = []
        for element in answered_list:
            client_dic = {"ip": element[1].psrc, "mac":element[1].hwsrc}
            client_list.append(client_dic)
        return client_list


    def print_list(result_list):
      print("-------------------------------------")
      print("IP\t\t\tMAC Address\n-------------------------------------")
      for client in result_list:
        print(client["ip"] + "\t\t" + client["mac"])



    scan_result = scan()
    print_list(scan_result)
ip()