#!/usr/bin/env python3
import argparse
from wifianalyzer import figlet
figlet()
def menu():
    print("\n****************************************************************")
    print("-------------------------")
    print("[1] Monitor-Mode")
    print("[2] Wifi-Scanning")
    print("[3] Monitor the Target")
    print("[4] DOS-ATTACK")
    print("[5] DDOS-ATTACK")
    print("[6] Fack_Authentication")
    print("[7] Manage-mode")
    print("[8] captureing-HandShake")
    print("[9] creating-wordlist")
    print("[10] crakeing-Password")
    print("[11] wps-scanning")
    print("[12] IP_Forwarding")
    print("[13] WPS_PIN_Attack")
    print("[14] Packet_sniff")
    print("[15] ARPSPOOF-ATTACK")
    print("[16] PORT Scanning")
    print("[17] APR_SPOOF Detector")
    print("[0] exit")
    print("-------------------------")
    print("\n****************************************************************")
menu()
inp = input("Enter the option: ")
option = int(inp)
while option != 0:
    if option == 1:
        from air import air
        air()
    elif option == 2:
       from thor import  scan
       scan()
    elif option == 3:
        from scan import scan
        scan()
    elif option == 4:
        from DOS import dos
        dos()
    elif option == 5: 
        from DDOS import ddauth 
        ddauth()
    elif option == 6:
        from fac import fac
        fac()
    elif option == 7:
        from mange import air
        air()
    elif option == 8:
        from handshake import scan
        scan()
    elif option == 9:
        from word_list import word
        word()
    elif option == 10:
        from password_cracking import crack
        crack()
    elif option == 11:
        from wps import wps
        wps()
    elif option == 12:
            from ip_forwarding import ipv4
            ipv4()
    elif option ==13:
        from wps_attack import rev
        rev()
    elif option == 14:
        from packet import packet
        packet()
    elif option == 15:
        from arpspoof import arp
        arp()
    elif option == 16:
        from port_scanner import port
        port()
    elif option == 17:   
        from arpspoof_detector import detect
        detect()
    else:    
        print("invalid input")              

   
    menu()
    option = int(input("enter the option:"))
