import argparse
import os
from fac_txt import fakeauth
fakeauth()
print("\n****************************************************************")
print("\n* Copyright of saai jeshwanth && nithesh, 2021 *")
print("\n****************************************************************")
def fac():

    bssid = input("enter the bssid :")
    mac= input("enter the MAC_address :")
    os.system(" aireplay-ng --fakeauth 30 -a " + bssid + " -h " + mac + " wlan0:")

