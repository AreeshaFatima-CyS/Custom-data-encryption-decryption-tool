🔐 Custom Data Encryption & Decryption Tool
A CLI-based Python tool that encrypts and decrypts text using a custom multi-layer algorithm. Built as part of Rhombix Technologies Internship – Task 3.

🎯 Objective
To simulate a real-world data protection system using custom cryptographic logic — not just basic base64 encoding.

⚙️ How the Encryption Works
The tool uses 3 layers of encryption:
LayerTechniqueDescription1️⃣Caesar CipherShifts each letter/digit by 7 positions2️⃣XOR CipherXORs the result with a secret key3️⃣Hex EncodingConverts final output to unreadable hex
Decryption simply reverses all 3 steps in order.

🖥️ Features

✅ Encrypt any plain text
✅ Decrypt encrypted hex text
✅ Save encrypted data to a JSON file (with timestamp)
✅ Load and decrypt saved data from file
✅ Clean CLI menu interface
✅ Error handling for invalid inputs


📋 Menu Options
1. Encrypt Data
2. Decrypt Data
3. Save Encrypted Data
4. Load & Decrypt Saved Data
5. Exit

🚀 How to Run
Requirements: Python 3.x (no extra libraries needed)
bashpython encryption_tool.py

💡 Example
Enter text to encrypt: Hello123

🔒 Encrypted: 3f7a9c2b1d...  (hex output)

🔓 Decrypted: Hello123
Saved file (encrypted_data.json) looks like:
json{
    "timestamp": "2024-06-07 14:30:00",
    "encrypted": "3f7a9c2b1d..."
}

📁 File Structure
├── encryption_tool.py      # Main Python script
├── encrypted_data.json     # Auto-generated when data is saved
└── README.md               # This file

👩‍💻 Author
Areesha Fatima
## 🎥 Demo Video

▶️ [Watch Demo Video]https://drive.google.com/file/d/1fGt4ciGeSzzQTVkwPAl-kSfN1EbbU6K6/view?usp=drive_link
Rhombix Technologies – Python Security Internship
Task 3: Custom Data Encryption & Decryption Tool
