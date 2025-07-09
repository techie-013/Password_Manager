# 🔐 Secure Password Manager (Python + Fernet Encryption)

This is a **simple and secure command-line password manager** built in Python. It uses the `cryptography` library's Fernet module to **encrypt and decrypt passwords**, ensuring your sensitive information is stored safely.

---

## 🚀 Features

- 🔐 Master password authentication
- 🔒 AES encryption using Fernet symmetric key
- 📝 Store and retrieve passwords for multiple accounts
- 📁 Automatically generates and saves encryption key (`key.key`)
- 📦 Lightweight and beginner-friendly

---

## 🛠 How It Works

1. The program checks if a `key.key` file (encryption key) exists. If not, it creates one.
2. It prompts for a master password. If incorrect, it exits securely.
3. You can choose to:
   - **Add** a new account and password
   - **View** all saved account passwords (decrypted)
4. Passwords are stored in `passwords.txt` in encrypted format.

---

## 📂 File Structure

```
.
├── Password_manager.py       # Main script
├── key.key                   # Fernet encryption key (auto-generated)
└── passwords.txt             # Encrypted password store
```

---

## 💻 Getting Started

### ✅ Prerequisites

- Python 3.x
- `cryptography` module

Install the required library:

```bash
pip install cryptography
```

---

### ▶️ Run the Script

```bash
python Password_manager.py
```

Follow the prompts:
- Enter your **master password** (`mysecret123` by default)
- Type `add`, `view`, or `q` as per your action

---

## 🔒 Example Output

```
Enter master password: ********

Enter new Password Or View Previous Ones (view,add) Or q to quit: add
Account Name : gmail
Enter your Password : myStrongPass
✅ Password saved successfully!

Enter new Password Or View Previous Ones (view,add) Or q to quit: view
User : gmail | Password : myStrongPass
```

---

## 📌 Possible Upgrades

- 🔍 Search for credentials by account name
- 🗑 Delete or update saved credentials
- 🔑 Add a password generator feature
- 🖥️ Create a basic GUI using Tkinter

---

## 📜 License

This project is licensed under the MIT

---

### ❤️ Made with love and Python by Sneha Singh
