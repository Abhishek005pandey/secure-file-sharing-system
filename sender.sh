#!/bin/bash
# sender.sh – Secure File Sender with automatic filename support

read -p "Enter receiver IP address: " RECIP
read -p "Enter file name to send: " FILE

if [[ ! -f "$FILE" ]]; then
  echo "❌ File '$FILE' not found!"
  exit 1
fi

echo
echo "🔍 Calculating SHA-256 checksum before sending:"
sha256sum "$FILE"

echo
echo "🚀 Sending '$FILE' securely to $RECIP..."
# Send filename first, then file data through OpenSSL
(
  echo "$FILE"
  cat "$FILE"
) | openssl s_client -quiet -connect ${RECIP}:4443 > /dev/null

echo "✅ File '$FILE' sent successfully!"
