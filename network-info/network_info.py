import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

print("=== Network Information ===")
print(f"Computer Name: {hostname}")
print(f"IP Address: {ip_address}")