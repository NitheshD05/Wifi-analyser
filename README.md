# WiFi Analyser

WiFi Analyzer is a comprehensive tool designed for network administrators and security professionals to monitor and analyze WiFi networks. It offers a wide range of functionalities, including WiFi scanning, monitoring, various types of attacks (DoS, DDoS, Fake Authentication, etc.), packet sniffing, port scanning, and more. The tool is intended for testing and securing wireless networks.

## Features

**Monitor Mode Activation:** Enables monitor mode on a specified network interface.

**WiFi Scanning:** Scans for available WiFi networks and displays detailed information.

**Target Monitoring:** Monitors a specific target (BSSID) on a specified channel.

**DoS and DDoS Attacks:** Conducts Denial of Service and Distributed Denial of Service attacks on specified targets.

**Fake Authentication:** Performs fake authentication against a specified WiFi network.

**Capture Handshakes:** Captures handshake packets for WPA/WPA2 networks.

**Wordlist Creation:** Generates wordlists using crunch for use in password cracking.

**Password Cracking**: Cracks WPA/WPA2 passwords using captured handshakes and wordlists.

**WPS Scanning and Attacks:** Scans for WPS-enabled networks and performs WPS PIN attacks using reaver.

**IP Forwarding:** Enables IP forwarding on the system.

**Packet Sniffing:** Sniffs network packets on a specified interface.

**ARP Spoofing:** Performs ARP spoofing attacks on a network.

**Port Scanning:** Scans specified IP address ranges for open ports.

**ARP Spoof Detection:** Detects ARP spoofing attacks on the network.

## Prerequisites
Ensure you have the following installed on your system:

Python 3.x - The Python programming language (version 3.x).

### Python Libraries:

**scapy:** A powerful Python library used for network packet manipulation.

**netifaces:** A library to get network interface information.

**termcolor:** A library for ANSI color formatting for terminal output.

**pyfiglet:** A Python library for creating ASCII art from text.

**python-nmap:** A Python library to interact with the Nmap port scanner.

### System Utilities:

**aircrack-ng:** A suite of tools for auditing wireless networks.

**reaver:** A tool for performing brute force attacks against WPS (Wi-Fi Protected Setup) registrar PINs.

**crunch:** A tool to generate custom wordlists for password cracking.

**dnsmasq:** A lightweight, easy-to-configure DNS forwarder and DHCP server.

**hostapd:** A user space daemon for access point and authentication servers.

## Installation

To use WiFi Analyser, follow these steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/NitheshD05/Wifi-analyser.git
   cd Wifi-analyser
   ```
2. Install the required Python packages:
   ```bash
   sudo apt-get update
   sudo apt-get install -y aircrack-ng reaver crunch dnsmasq hostapd
   pip install -r requirements.txt
   ```
4. ## Usage
Run the main script opt.py to start the WiFi Analyzer tool and access the menu options:
```bash
python3 opt.py
```
### Menu Options
```bash
****************************************************************
-------------------------
[1] Monitor-Mode
[2] Wifi-Scanning
[3] Monitor the Target
[4] DOS-ATTACK
[5] DDOS-ATTACK
[6] Fake_Authentication
[7] Manage-mode
[8] Capturing-HandShake
[9] Creating-Wordlist
[10] Cracking-Password
[11] WPS-Scanning
[12] IP_Forwarding
[13] WPS_PIN_Attack
[14] Packet_sniff
[15] ARPSPOOF-ATTACK
[16] PORT Scanning
[17] ARP_SPOOF Detector
[0] Exit
-------------------------
****************************************************************
```


## Disclaimer

This tool is intended for educational purposes only. The authors are not responsible for any misuse or damage caused by this tool. Use it responsibly and only on networks you own or have permission to test.
