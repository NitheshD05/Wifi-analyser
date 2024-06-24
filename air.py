import subprocess as sub
import time
from air_txt import airmon
airmon()
def air():
     print("\n****************************************************************")
     print("\n* Copyright of saai jeshwanth && nithesh, 2021                              *")
     print("\n****************************************************************")
     Interface = input("Enter the interface Change to Monitor-mode: ")
     sub.call("airmon-ng start " + Interface, shell=True)