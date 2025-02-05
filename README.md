# IP Scanner

## Description
This Python script takes a CIDR notation input, calculates the network range based on the subnet mask, iterates over all valid host addresses in the range, and reports which IP addresses successfully respond to ping requests.

## Installation & Dependencies
### Prerequisites
- Python 3.x
- Works on Windows, macOS, and Linux
- Ensure `ping` is accessible from the command line

### Installation
1. Clone the repository or download the script:
   ```bash
   git clone https://github.com/yourusername/network-scanner.git
   cd network-scanner
   ```
2. Run the script:
   ```bash
   python3 network_scan.py
   ```

## Usage
### Running the Script
1. Open a terminal and navigate to the script's directory.
2. Execute the script:
   ```bash
   python3 network_scan.py
   ```
3. Enter the CIDR notation when prompted, e.g.,:
   ```
   Enter CIDR notation (e.g., 192.168.1.0/24): 192.168.1.0/24
   ```
4. The script will scan the provided range and display live hosts.

### Example Output
```
Scanning network: 192.168.1.0/24
[-] No response: 192.168.1.1
[+] Host is up: 192.168.1.2
[+] Host is up: 192.168.1.5
...
Live hosts found:
192.168.1.2
192.168.1.5
```

## Error Handling & Validation
- **Invalid CIDR Notation**: The script checks for correct CIDR format and informs the user if invalid.
- **Ping Failures**: If a device does not respond, it is marked as inactive.
- **Permissions**: On Unix-based systems, you may need `sudo` to run:
- **CIDR Range**: The script will not attempt to scan beyond the network's broadcast address.
- **Scanning all hosts**: If script begins to scan all hosts then exit terminal
  ```bash
  sudo python3 network_scan.py
  ```

## Troubleshooting
- **No hosts detected?**
  - Ensure the network is active.
  - Check if firewalls are blocking ICMP requests.
- **Permission Issues?**
  - Run the script with `sudo` on Linux/macOS.

## License
This project is licensed under the MIT License.

