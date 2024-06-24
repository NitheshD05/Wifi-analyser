#!/usr/bin/env python3
import argparse
import os
from wordlist_txt import wordlist
wordlist()
def word():
    print("\n****************************************************************")
    print("\n* Copyright of saai jeshwanth && nithesh, 2021 *")
    print("\n****************************************************************")

    min = input("enter the minimum no :")
    max = input("enter the max no :")
    file_name = input("Enter the file_name :")
    condition1 = input("Enter the condition : ")
    condition2 = input("Enter the condition2 :")
    os.system(" crunch "+  min + " " + max + " " + condition1 + " -o " + file_name + " -t " + condition2 + " wlan0 ")
    