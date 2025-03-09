#!/usr/bin/env python3

import sys
import subprocess
import getpass

def decrypt_file(encrypted_file, output_file):
    password = getpass.getpass("Enter password for decryption: ")

    command = [
        "openssl", "enc", "-aes-256-cbc", "-d", "-salt", "-iter", "100000", "-pbkdf2",
        "-in", encrypted_file, "-out", output_file, "-pass", f"pass:{password}"
    ]
    
    result = subprocess.run(command, stderr=subprocess.PIPE, text=True)

    if result.returncode == 0:
        print(f"[✅] File decrypted: {output_file}")
    else:
        print("[❌] Decryption failed. Check your password or file.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: cipherguard_decrypt <encrypted_file> <output_file>")
        sys.exit(1)

    decrypt_file(sys.argv[1], sys.argv[2])