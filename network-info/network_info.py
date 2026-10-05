import socket
import subprocess

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

gateway = "not detected"

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

print("=== Network Information ===")
print(f"Computer Name: {hostname}")
print(f"IP Address: {ip_address}")
print(f"default Gateway: {gateway}")