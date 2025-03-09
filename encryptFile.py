#!/usr/bin/env python3

import sys
import subprocess
import getpass

def encrypt_file(input_file, output_file):
    password = getpass.getpass("Enter password: ")
    confirm_password = getpass.getpass("Confirm password: ")

    if password != confirm_password:
        print("[❌] Passwords do not match. Encryption aborted.")
        sys.exit(1)

    command = [
        "openssl", "enc", "-aes-256-cbc", "-salt", "-iter", "100000", "-pbkdf2",
        "-in", input_file, "-out", output_file, "-pass", f"pass:{password}"
    ]
    
    subprocess.run(command)
    print(f"[✅] File encrypted: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: cipherguard <input_file> <output_file>")
        sys.exit(1)

    encrypt_file(sys.argv[1], sys.argv[2])