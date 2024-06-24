#!/usr/bin/env python3
import os
def scan():
    bssid = input("enter the bssid :")
    channel_no = input("enter the channel no :")
    Interface = input("Enter the interface in monitor mode: ")
    os.system(" airodump-ng --bssid " + bssid + " -c " +  channel_no  + " " + Interface )
