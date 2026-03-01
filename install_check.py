import subprocess
import sys

reqs_file = "/opt/odoo/requirements.txt"
try:
    # Try to use pip to show what would be installed
    # If the output contains 'Would install', requirements are missing
    result = subprocess.run([sys.executable, "-m", "pip", "install", "--dry-run", "--report", "-", "-r", reqs_file], capture_output=True, text=True)
    if "install" in result.stdout:
        print("Missing requirements")
    else:
        print("All satisfied")
except Exception as e:
    print(f"Error: {e}")
