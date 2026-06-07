import json
import os
from datetime import datetime
# ─── Encryption Key ───────────────────────────────────────────
SHIFT = 7
SECRET_KEY = "rhombix2024"
# ─── Encrypt ──────────────────────────────────────────────────
def encrypt(text):
    # Step 1: Caesar shift
    shifted = ""
    for ch in text:
        if ch.isalpha():
            base = ord('A') if ch.isupper() else ord('a')
            shifted += chr((ord(ch) - base + SHIFT) % 26 + base)
        elif ch.isdigit():
            shifted += str((int(ch) + SHIFT) % 10)
        else:
            shifted += ch
    # Step 2: XOR with secret key
    key_bytes = SECRET_KEY * (len(shifted) // len(SECRET_KEY) + 1)
    xored = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(shifted, key_bytes))
    # Step 3: Reverse the string
    final = xored[::-1]
    # Convert to hex so it looks unreadable
    return final.encode().hex()
# ─── Decrypt ──────────────────────────────────────────────────
def decrypt(hex_text):
    try:
        # Step 1: Hex back to string
        raw = bytes.fromhex(hex_text).decode()
        # Step 2: Reverse
        reversed_text = raw[::-1]
        # Step 3: XOR undo (XOR is its own inverse)
        key_bytes = SECRET_KEY * (len(reversed_text) // len(SECRET_KEY) + 1)
        unxored = ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(reversed_text, key_bytes))
        # Step 4: Undo Caesar shift
        original = ""
        for ch in unxored:
            if ch.isalpha():
                base = ord('A') if ch.isupper() else ord('a')
                original += chr((ord(ch) - base - SHIFT) % 26 + base)
            elif ch.isdigit():
                original += str((int(ch) - SHIFT) % 10)
            else:
                original += ch
        return original
    except Exception:
        return None
# ─── Save to File ─────────────────────────────────────────────
def save_data(encrypted_text):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {"timestamp": timestamp, "encrypted": encrypted_text}
    filename = "encrypted_data.json"
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)
    print(f"\n✅ Data saved to '{filename}'")
# ─── Load from File ───────────────────────────────────────────
def load_data():
    filename = "encrypted_data.json"
    if not os.path.exists(filename):
        print("\n❌ No saved file found.")
        return
    with open(filename, "r") as f:
        data = json.load(f)
    enc = data["encrypted"]
    time = data["timestamp"]
    print(f"\n📂 Loaded encrypted data (saved at {time})")
    print(f"🔒 Encrypted: {enc}")
    result = decrypt(enc)
    if result:
        print(f"🔓 Decrypted: {result}")
    else:
        print("❌ Could not decrypt the loaded data.")
# ─── Main Menu ────────────────────────────────────────────────
def main():
    print("=" * 45)
    print("   🔐 Custom Encryption & Decryption Tool")
    print("=" * 45)
    last_encrypted = None
    while True:
        print("\n📋 Menu:")
        print("  1. Encrypt Data")
        print("  2. Decrypt Data")
        print("  3. Save Encrypted Data")
        print("  4. Load & Decrypt Saved Data")
        print("  5. Exit")
        choice = input("\nEnter choice (1-5): ").strip()
        if choice == "1":
            text = input("Enter text to encrypt: ").strip()
            if not text:
                print("❌ Please enter some text.")
                continue
            last_encrypted = encrypt(text)
            print(f"\n🔒 Encrypted: {last_encrypted}")
        elif choice == "2":
            enc = input("Enter encrypted text (hex): ").strip()
            if not enc:
                print("❌ Please enter encrypted text.")
                continue
            result = decrypt(enc)
            if result:
                print(f"\n🔓 Decrypted: {result}")
            else:
                print("❌ Invalid encrypted text.") 
        elif choice == "3":
            if not last_encrypted:
                print("❌ Encrypt something first (Option 1).")
            else:
                save_data(last_encrypted)
        elif choice == "4":
            load_data()
        elif choice == "5":
            print("\n👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Enter 1-5.")
if __name__ == "__main__":
    main()