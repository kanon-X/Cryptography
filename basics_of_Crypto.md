# 🔐 CRYPTOGRAPHY

## What is Cryptography?
Cryptography is a method to secure communication from unauthorized parties.

---

## 🎯 Cryptography Goals

1. **Confidentiality**  
   Protects the secrecy of information. Even if the transmission or storage medium is compromised, encrypted data remains useless to unauthorized users.

2. **Integrity**  
   Ensures information has not been tampered with, typically using hashing methods.

3. **Authenticity**  
   Verifies that the information is from the intended sender using digital certificates, digital signatures, and Public Key Infrastructure (PKI).

---

## 🔑 Types of Cryptography

### 1. Symmetric Cryptography (Secret Key)
- Both sender and receiver use the **same secret key** to encrypt and decrypt data.
- Common algorithms: Blowfish, AES, RC4, DES, RC5, RC6
- AES variants: AES-128, AES-192, AES-256 (all use 128-bit block size)

### 2. Asymmetric Cryptography (Public Key)
- Uses a **key pair**: public key and private key.
- Public key encrypts, private key decrypts — and vice versa.
- Common algorithms: RSA, ELC, Diffie-Hellman

---

## 🔐 Asymmetric Cryptography Usages

### ✅ Data Encryption
- Sender encrypts data with **receiver’s public key**.
- Receiver decrypts with **own private key**.

#### 🔄 Encrypting a Message
1. Sender encrypts document with a one-time symmetric key (e.g., AES or DES).
2. Sender encrypts the symmetric key with receiver’s public key.
3. Sender sends both encrypted document and encrypted key.

#### 🔓 Decrypting a Message
1. Receiver decrypts the session key using their private key.
2. Receiver uses the session key to decrypt the document.

---

## ✍️ Digital Signature

- A digital signature is the **encryption of a hash** using the sender’s **private key**.

### 🔍 Verifying a Digital Signature
1. Receiver decrypts the signature using sender’s public key → gets the hashed message.
2. Receiver hashes the original message.
3. Compares both hashes for verification.

---

## 🔁 What is Hashing?

- Converts input data into a fixed-size digest.
- **One-way function**: original input cannot be derived from the hash.
- Used for securely storing passwords.

### Common Hashing Algorithms:
- MD5
- SHA-1
- SHA-2
- SHA-3
- bcrypt
- Whirlpool

---

## 🧂 Enhance Hash Flavor with Salt and Pepper

### 🌈 Rainbow Table Attack
- Precomputed hashes for common passwords.
- If hashes are predictable, attackers can match them to known inputs.

### 🧂 Salt
- A random string added to the password before hashing.
- Stored alongside the hash in the database.
- Forces attackers to regenerate rainbow tables for each salt.

### 🌶️ Pepper
- A secret string added to the password before hashing.
- **Not stored** in the database.
- During login, the system tries known pepper values to find a match.

---

## 🏛️ What is Public Key Infrastructure (PKI)?

- A framework using public key cryptography for **authentication** and **confidentiality**.
- Uses **digital certificates** (X.509 standard) issued by trusted Certificate Authorities (CAs) like DigiCert or VeriSign.

### 🔐 PKI Workflow
1. Sender requests receiver’s certificate from CA.
2. Extracts receiver’s public key from certificate.
3. Encrypts message and sends it.
4. Receiver decrypts using private key.

### 🌐 PKI in HTTPS
- Browser requests SSL certificate from server.
- Verifies certificate via trusted CA.
- Extracts server’s public key.
- Starts encrypted session using TLS/SSL.
- Sends sensitive data (e.g., credit card info) securely.

---

## 🤝 Why Combine Symmetric and Asymmetric Cryptography?

We combine both for **best security and performance**:

- **Symmetric**: Fast for encrypting large data.
- **Asymmetric**: Secure for key exchange and authentication.

### 🔄 Hybrid Encryption
- Encrypt data with symmetric key (AES).
- Encrypt symmetric key with receiver’s public key (RSA).
- Send both → receiver decrypts symmetric key → decrypts data.

This combo is called **hybrid encryption** — the strongest and most efficient approach.

---

## 🛡️ Pepper Protection in Password Hashing

Even if a hacker gains access to:
- Hashed passwords
- Salt values
- Hashing algorithm

They **still can't crack passwords easily** if a pepper is used.

### ✅ Why Pepper Helps
- Adds a secret layer not stored in the database.
- Prevents brute-force and rainbow table attacks.

### ⚠️ Limitations of Pepper
- If leaked, all passwords are vulnerable.
- Changing the pepper requires rehashing all passwords.
- Must be stored securely in app or hardware.
- If app is compromised, pepper may be exposed.

