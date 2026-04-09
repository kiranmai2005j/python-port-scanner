import socket
import datetime

# Common ports and the services they usually run
COMMON_PORTS = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    135: "RPC",
    139: "NetBIOS",
    143: "IMAP",
    443: "HTTPS",
    445: "SMB",
    3306: "MySQL",
    3389: "RDP",
    5900: "VNC",
    8080: "HTTP-Alt",
    8443: "HTTPS-Alt",
    27017: "MongoDB",
    5432: "PostgreSQL",
    6379: "Redis"
}

def scan_port(target, port, timeout=1):
    # Try to open a TCP connection to the port
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((target, port))
        sock.close()
        return result == 0  # 0 means connection succeeded = port open
    except:
        return False

def run_scanner(target):
    # Resolve hostname to IP address
    try:
        ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: Could not resolve hostname '{target}'")
        return

    print(f"\n{'='*45}")
    print(f" Port Scanner — Target: {ip}")
    print(f" Started: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"{'='*45}")

    open_ports = []

    for port, service in COMMON_PORTS.items():
        print(f"Scanning port {port} ({service})...", end="\r")
        if scan_port(ip, port):
            open_ports.append((port, service))
            print(f"  [OPEN]   Port {port:<6} — {service}")

    print(f"\n{'='*45}")
    print(f" Scan complete. {len(open_ports)} open port(s) found.")
    print(f"{'='*45}\n")

# Entry point
target = input("Enter target IP or hostname: ")
run_scanner(target)
