import os
def scan():
    print("\n****************************************************************")
    print("\n* Copyright of saai jeshwanth && nithesh, 2021 *")
    print("\n****************************************************************")
    bssid = input("enter the bssid :")
    channel_no = input("enter the channel no :")
    filename_only = input("Enter the FileName :")
    
    os.system(" airodump-ng --bssid " + bssid + " -c " + channel_no + " " "-w " + filename_only + " wlan0 ")
    
