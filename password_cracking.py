import os

def crack():
    handshake_filename = input("Enter the handshake file_name :")
    wordlist_filename = input("Enter the wordlist Filename :")
    os.system(" aircrack-ng " + handshake_filename + " -w "+ wordlist_filename)
    