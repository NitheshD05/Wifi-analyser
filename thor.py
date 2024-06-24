import os
def scan():
    print("\n****************************************************************")
    print("\n* Copyright of saai jeshwanth && nithesh, 2021 *")
    print("\n****************************************************************")
    Interface = input("Enter the interface in monitor mode: ")
    os.system("sudo ifconfig " + Interface + " down ")
    os.system("sudo iwconfig wlan0 " + Interface + "mode monitor")
    os.system("sudo ifconfig" + Interface + " up ")
    os.system("sudo airodump-ng " + Interface )
    