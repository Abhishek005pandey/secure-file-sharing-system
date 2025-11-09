# 🔒 Secure File Sharing System (Python + TLS)

A simple yet powerful project that demonstrates **secure, encrypted file transfer** between two systems using **Python** and **OpenSSL’s TLS**.  
Ensures complete **data confidentiality and integrity** using encryption (TLS) and verification (SHA-256).

---

## 📘 Features

- ✅ End-to-end encryption using TLS (AES-256-GCM)
- ✅ Secure transmission between sender and receiver
- ✅ Automatic filename detection and saving
- ✅ Works for all file types (text, images, PDFs, zip, etc.)
- ✅ SHA-256 integrity verification after transfer
- ✅ Fully automated (no manual steps or Ctrl+C)

---

## ⚙️ Technologies Used

- **Python 3**
- **OpenSSL / TLS**
- **Socket Programming**
- **Ubuntu / Linux**
- **SHA-256 Hashing**

---

## 🧩 System Architecture

┌──────────────┐ ┌──────────────┐
│ sender.py │ │ receiver.py │
│ │ Encrypted TLS Link │ │
│ file.txt ───────────────────────────▶ │ Saves file │
│ │ (Port 4443, TLS) │ SHA256 ✅ │
└──────────────┘ └──────────────┘

yaml
Copy code

---

## 🖥️ Setup & Usage

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/secure-file-sharing-system.git
cd secure-file-sharing-system
2️⃣ Generate certificate & key (on receiver)
bash
Copy code
openssl req -x509 -newkey rsa:4096 -nodes -sha256 \
  -keyout server.key -out server.crt -days 365 \
  -subj "/C=IN/ST=Maharashtra/L=Pune/O=MyOrg/OU=IT/CN=receiver.local"
3️⃣ Start the receiver
bash
Copy code
python3 receiver.py
4️⃣ Send a file from sender
bash
Copy code
python3 sender.py
Enter:

php-template
Copy code
Enter receiver IP address: <Receiver_IP>
Enter file to send: <filename>
✅ Output shows file received successfully with matching SHA-256 hash.

📂 Example
Receiver output:

csharp
Copy code
📡 Connection from: ('192.168.16.128', 56900)
📁 Receiving file: test_image.jpg
✅ File 'test_image.jpg' received successfully!
🔍 SHA-256 checksum:
d5498914d6f249724f38281f459026b13e022bec302176000434361cd6fa50ab  test_image.jpg
🧾 Project Outcomes
Demonstrated confidentiality (encrypted transfer)

Demonstrated integrity (verified SHA-256)

Implemented secure file transfer using Python TLS

Supports all file types

🚀 Future Enhancements
Add progress bar for large file transfers

Add GUI interface for sender/receiver

Add multi-file or folder transfer support

Add digital signature verification

👨‍💻 Author
Abhishek Pandey
