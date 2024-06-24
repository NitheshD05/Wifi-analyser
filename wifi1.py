import sys 
from scapy.all import *
  
IFACE_NAME = "wlan0"
devices = set() 
print("\n****************************************************************")
print("\n* Copyright of saai jeshwanth && nithesh, 2021 *")
print("\n****************************************************************")
  
def PacketHandler(pkt): 
    if pkt.haslayer(Dot11): 
        dot11_layer = pkt.getlayer(Dot11) 
          
        if dot11_layer.addr2 and (dot11_layer.addr2 not in devices): 
            devices.add(dot11_layer.addr2) 
            print(len(devices), dot11_layer.addr2, dot11_layer.payload.name) 
  
  
sniff(iface=IFACE_NAME, count=1, prn=PacketHandler)