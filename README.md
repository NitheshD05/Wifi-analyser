# WiFi Analyser

WiFi Analyser is a penetration testing tool designed to assess the security of WiFi networks. Developed in Python 3 and customized for Kali Linux, this tool is intended to be used in the Linux terminal for evaluating the security posture of targeted WiFi networks.

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

#### Python Libraries:

**scapy:** A powerful Python library used for network packet manipulation.

**netifaces:** A library to get network interface information.

**termcolor:** A library for ANSI color formatting for terminal output.

**pyfiglet:** A Python library for creating ASCII art from text.

**python-nmap:** A Python library to interact with the Nmap port scanner.

#### System Utilities:

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

## Details
**1. Monitor Mode Activation**

Activates monitor mode on a specified network interface. This mode allows the interface to capture all packets in the vicinity, including those not addressed to the device. Essential for network analysis and packet sniffing.

**2. WiFi Scanning**

Scans for available WiFi networks and displays detailed information. Includes BSSID, signal strength, channel, and encryption type. Helps identify nearby networks and their characteristics.

**3. Target Monitoring**

Monitors a specific target (BSSID) on a specified channel. Provides real-time updates on the target's activity, such as packet count and signal strength. Useful for tracking a particular device.

**4. DoS Attack**

Conducts a Denial of Service attack on a specified target. Disrupts the target's network connectivity by overwhelming it with requests. Effective for testing network robustness.

**5. DDoS Attack**

Performs a Distributed Denial of Service attack using multiple devices. Floods the target with excessive traffic, causing network disruptions. Useful for stress-testing network defenses.

**6. Fake Authentication**

Attempts fake authentication against a specified WiFi network. Tries to associate with the access point without needing a valid password. Helps in testing network security.

**7. Manage Mode**

Switches the network interface back to managed mode from monitor mode. Restores normal network operation, allowing the device to connect to WiFi networks. Ensures seamless network transitions.

**8. Capturing Handshakes**

Captures WPA/WPA2 handshake packets for offline password cracking. Essential for testing network security by attempting to recover passwords from captured handshakes.

**9. Creating Wordlist**

Generates custom wordlists using crunch based on specified parameters. Creates tailored lists of potential passwords for use in brute force attacks. Supports various customization options.

**10. Cracking Password**

Cracks WPA/WPA2 passwords using captured handshakes and wordlists. Employs brute force or dictionary attacks to recover network passwords. Validates network security measures.

**11. WPS Scanning**

Scans for WPS-enabled networks, providing details on their WPS capabilities. Identifies networks that may be vulnerable to WPS-based attacks. Helps in assessing network security.

**12. IP Forwarding**

Enables IP forwarding on the system, allowing packet forwarding between interfaces. Facilitates network routing and bridging. Essential for certain network configurations and attacks.

**13. WPS PIN Attack**

Uses reaver to perform a WPS PIN attack, brute forcing the WPS PIN. Attempts to gain access to the network by exploiting WPS vulnerabilities. Tests the security of WPS-enabled networks.

**14. Packet Sniffing**

Sniffs network packets on a specified interface, capturing data for analysis. Useful for monitoring network traffic and identifying potential issues or attacks.

**15. ARP Spoofing**

Performs ARP spoofing attacks, redirecting network traffic through the attacker’s machine. Useful for man-in-the-middle attacks and network traffic interception.

**16. Port Scanning**

Scans specified IP ranges for open ports, revealing available services. Identifies potential security vulnerabilities by detecting open ports and running services.

**17. ARP Spoof Detection**

Detects ARP spoofing attacks on the network, alerting users to potential threats. Helps in maintaining network security by identifying malicious activities.


## Disclaimer

This tool is intended for educational purposes only. The authors are not responsible for any misuse or damage caused by this tool. Use it responsibly and only on networks you own or have permission to test.
