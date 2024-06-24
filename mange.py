import subprocess as sub
import time
from manage_txt import airmon_ng
airmon_ng()
def air():
    print("\n****************************************************************")
    print("\n* Copyright of saai jeshwanth && nithesh, 2021 *")
    print("\n****************************************************************")
    sub.call(['airmon-ng', 'stop', 'wlan0'])
