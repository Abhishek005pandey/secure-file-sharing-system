import ssl
import socket

# TLS server setup
context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile="server.crt", keyfile="server.key")

HOST = "0.0.0.0"   # Listen on all interfaces
PORT = 4443

print("🔒 Secure Receiver started...")
print(f"Listening on port {PORT}...")

with socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0) as sock:
    sock.bind((HOST, PORT))
    sock.listen(1)
    conn, addr = sock.accept()
    print(f"📡 Connection from: {addr}")

    with context.wrap_socket(conn, server_side=True) as tls:
        # Receive the filename first
        filename = tls.recv(1024).decode().strip()
        print(f"📁 Receiving file: {filename}")

        # Receive file content
        with open(filename, 'wb') as f:
            while True:
                data = tls.recv(4096)
                if not data:
                    break
                f.write(data)

        print(f"✅ File '{filename}' received successfully!")

        # Verify integrity (optional)
        import subprocess
        result = subprocess.run(['sha256sum', filename], capture_output=True, text=True)
        print(f"🔍 SHA-256 checksum:\n{result.stdout}")
