#!/usr/bin/env bash
set -euo pipefail

PORT="${1:-8000}"
PAGE="${2:-index.html}"

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

is_port_free() {
  python3 - "$1" <<'PY'
import socket, sys
port = int(sys.argv[1])
s = socket.socket()
try:
    s.bind(("127.0.0.1", port))
    print("free")
except OSError:
    print("busy")
finally:
    s.close()
PY
}

PORT_RESULT="$(is_port_free "$PORT")"
if [ "$PORT_RESULT" != "free" ]; then
  for candidate in $(seq $((PORT + 1)) $((PORT + 20))); do
    if [ "$(is_port_free "$candidate")" = "free" ]; then
      PORT="$candidate"
      break
    fi
  done
fi

if command -v xdg-open >/dev/null 2>&1; then
  xdg-open "http://localhost:${PORT}/${PAGE}" >/dev/null 2>&1 || true
elif command -v open >/dev/null 2>&1; then
  open "http://localhost:${PORT}/${PAGE}" >/dev/null 2>&1 || true
fi

echo "Serving ${ROOT_DIR} on http://localhost:${PORT}/ (page: ${PAGE})"
cd "${ROOT_DIR}"
if ! python3 -m http.server "${PORT}"; then
  echo "Server failed to start. Press Enter to close."
  read -r _
fi
