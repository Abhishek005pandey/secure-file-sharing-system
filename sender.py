import ssl
import socket
import os

receiver_ip = input("Enter receiver IP address: ").strip()
file_path = input("Enter file to send: ").strip()

if not os.path.isfile(file_path):
    print("❌ File not found!")
    exit(1)

# TLS client setup
context = ssl.create_default_context()
context.check_hostname = False
context.verify_mode = ssl.CERT_NONE

print(f"🔍 Calculating SHA-256 before sending:")
os.system(f"sha256sum {file_path}")

with socket.create_connection((receiver_ip, 4443)) as sock:
    with context.wrap_socket(sock, server_hostname=receiver_ip) as tls:
        # Send filename first
        filename = os.path.basename(file_path)
        tls.sendall((filename + "\n").encode())

        # Send file content
        with open(file_path, 'rb') as f:
            tls.sendfile(f)

print(f"✅ File '{file_path}' sent securely!")
