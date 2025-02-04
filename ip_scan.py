import ipaddress
import subprocess
import platform

def get_live_hosts(cidr):
    try:
        network = ipaddress.IPv4Network(cidr, strict=False)
    except ValueError as e:
        print(f"Error: {e}")
        return

    live_hosts = []
    print(f"Scanning network: {cidr}")

    for ip in network.hosts():  # Excludes network and broadcast addresses
        ip_str = str(ip)
        if ping(ip_str):
            live_hosts.append(ip_str)
            print(f"[+] Host is up: {ip_str}")
        else:
            print(f"[-] No response: {ip_str}")

    print("\nLive hosts found:")
    for host in live_hosts:
        print(host)

def ping(ip):
    """Send a ping request to the given IP address and return True if it responds."""
    param = "-n" if platform.system().lower() == "windows" else "-c"
    try:
        result = subprocess.run(
            ["ping", param, "1", "-W", "1", ip],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )
        return result.returncode == 0
    except Exception:
        return False

if __name__ == "__main__":
    cidr_input = input("Enter CIDR notation (e.g., 192.168.1.0/24): ").strip()
    get_live_hosts(cidr_input)