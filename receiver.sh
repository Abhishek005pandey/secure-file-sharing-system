#!/bin/bash
# receiver.sh – reliable version

echo "🔒 Starting secure receiver on port 4443..."
echo "Waiting for connection..."

# start server, write everything to a temp file
TMPFILE=$(mktemp)
openssl s_server -quiet -accept 4443 -cert server.crt -key server.key >"$TMPFILE" 2>/dev/null

# now extract first line as filename
FILENAME=$(head -n 1 "$TMPFILE" | tr -d '\r')
# and the rest as the actual data
tail -n +2 "$TMPFILE" > "$FILENAME"

rm -f "$TMPFILE"

echo
echo "✅ File received successfully!"
echo "📄 Saved as: $FILENAME"
echo
echo "🔍 Calculating SHA-256 checksum:"
sha256sum "$FILENAME"
