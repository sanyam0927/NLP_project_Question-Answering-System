"""
Main entrypoint to launch the Extractive Question Answering System application.
"""

import os
import sys
import webbrowser
from pathlib import Path

# Add project root to path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from src.web_server import run_server


def main():
    host = os.environ.get("HOST", "127.0.0.1")
    port = int(os.environ.get("PORT", 8080))

    print("\n" + "=" * 70)
    print("   Starting Question Answering System (SQuAD 2.0)")
    print("=" * 70)
    print(f"[*] Project directory: {Path(__file__).resolve().parent}")
    print(f"[*] Server listening:  http://{host}:{port}")
    print(f"[*] Open your browser at http://{host}:{port} to access the GUI.")
    print("=" * 70 + "\n")

    # Launch server
    run_server(host=host, port=port)


if __name__ == "__main__":
    main()
