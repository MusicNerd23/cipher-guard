# 🚀 CipherGuard - Secure File Encryption & Decryption
🔐 **GitHub Repository:** [CipherGuard](https://github.com/MusicNerd23/cipher-guard)

---

## 🛡 CipherGuard: AES-256 File Encryption Tool
CipherGuard is a **lightweight, command-line tool** that securely encrypts and decrypts files using **AES-256-CBC encryption** powered by OpenSSL. Designed for security professionals, developers, and anyone who needs **strong file encryption**.

![Encryption](https://img.shields.io/badge/Encryption-AES--256--CBC-blue) ![Language](https://img.shields.io/badge/Made%20with-Python-orange)

---

## 🚀 Features
✅ **AES-256-CBC Encryption & Decryption** (Industry-standard security)  
✅ **Password Confirmation for Encryption** (Prevents mistyped passwords)  
✅ **Command-Line Interface (CLI)** (Fast & easy terminal usage)  
✅ **Cross-Platform** (Works on macOS & Linux)  
✅ **Integrated with `/usr/local/bin/`** (Run as a system command)  

---

## 📌 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/MusicNerd23/cipher-guard.git
cd cipher-guard
```

### 2️⃣ Make Scripts Executable
```sh
chmod +x cipherguard_encrypt.py cipherguard_decrypt.py
```

### 3️⃣ Move to `/usr/local/bin/` for Global Use
```sh
sudo mv cipherguard_encrypt.py /usr/local/bin/cipherguard_encrypt
sudo mv cipherguard_decrypt.py /usr/local/bin/cipherguard_decrypt
```

---

## 🚀 Usage
### 🔹 Encrypt a File
```sh
cipherguard_encrypt secret.txt secret.enc
```
- **Prompts for a password** (hides input for security)  
- **Confirms password before encrypting**  
- **Saves encrypted file as `secret.enc`**  

### 🔹 Decrypt a File
```sh
cipherguard_decrypt secret.enc decrypted.txt
```
- **Prompts for password** (must match encryption password)  
- **Restores original file as `decrypted.txt`**  

---

## 🛠 How It Works
- Uses **AES-256-CBC encryption** with **PBKDF2 key derivation** for security.  
- Relies on **OpenSSL** to handle encryption efficiently.  
- Prevents errors by **confirming passwords before encryption**.  

---

## 📌 Example Usage
```sh
cipherguard_encrypt mynotes.txt mynotes.enc
# Enter password:
# Confirm password:
# [✅] File successfully encrypted: mynotes.enc
```

```sh
cipherguard_decrypt mynotes.enc mynotes.txt
# Enter password:
# [✅] File successfully decrypted: mynotes.txt
```

---

## 📂 File Structure
```
cipherguard/
│── cipherguard_encrypt.py   # Encryption script
│── cipherguard_decrypt.py   # Decryption script
│── README.md                # Project documentation
```

---

## 🛡 Security Notice
- **Do not share your password** with anyone.  
- **Encrypted files cannot be recovered without the correct password.**  
- **Use strong passwords** to ensure maximum security.  

---

## 👨‍💻 Contributing
Want to improve CipherGuard?  
- Fork the repository 🍴  
- Create a new branch 🌱  
- Make improvements & submit a PR 🚀  

---

## 📜 License
This project is licensed under the **MIT License**.

---