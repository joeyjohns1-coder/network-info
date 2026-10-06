import socket
import subprocess

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
dns_name = socket.getfqdn()
gateway = "not detected"
dns_server = "not detected"
result = subprocess.run(
    ["ipconfig"],
    capture_output=True,
    text=True
          )

for line in result.stdout.splitlines():
    if "Default Gateway" in line:
        gateway = line.split(":")[-1].strip()
        if gateway:
            break        
dns_found = False

# DNS detection
dns_result = subprocess.run(
    [
        "powershell",
        "-Command",
        "(Get-DnsClientServerAddress | Select-Object -ExpandProperty ServerAddresses)"
    ],
    capture_output=True,
    text=True
)

dns_servers = [
    line.strip()
    for line in dns_result.stdout.splitlines()
    if line.strip()
]

ipv4_dns = []
ipv6_dns = []

for server in dns_servers:
    if ":" in server and not server.lower().startswith("fec0"):
        ipv6_dns.append(server)
    elif "." in server:
        ipv4_dns.append(server)

ipv4_dns_display = ", ".join(ipv4_dns) if ipv4_dns else "Not detected"
ipv6_dns_display = ", ".join(ipv6_dns) if ipv6_dns else "Not detected"


if not ipv4_dns and not ipv6_dns:
    dns_server = "not detected"

print("=== Network Information ===")
print(f"Computer Name: {hostname}")
print(f"IP Address: {ip_address}")
print(f"DNS Name: {dns_name}")
print(f"default Gateway: {gateway}")
print(f"IPv4 DNS Server: {ipv4_dns_display}")
print(f"IPv6 DNS Server: {ipv6_dns_display}")