#!/usr/bin/env python3
import os
from ip_txt import ip
ip()
print("\n****************************************************************")
print("\n* Copyright of saai jeshwanth && nithesh, 2021                              *")
print("\n****************************************************************")

def ipv4():
    ip = os.system("echo 1 >/proc/sys/net/ipv4/ip_forward ")
    print("IP_FORWARDING DONE ")
