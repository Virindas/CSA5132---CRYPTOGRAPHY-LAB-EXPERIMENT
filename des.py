from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

def encrypt_des(text, key):
    # DES key must be exactly 8 bytes (64 bits)
    des_key = key.encode('utf-8')
    # Create DES cipher object in Electronic Codebook (ECB) mode
    cipher = DES.new(des_key, DES.MODE_ECB)
    
    # Pad text to be multiple of 8 bytes (DES block size)
    padded_text = pad(text.encode('utf-8'), DES.block_size)
    encrypted_bytes = cipher.encrypt(padded_text)
    
    # Return result as a hex string for easy reading
    return encrypted_bytes.hex()

def decrypt_des(hex_ciphertext, key):
    des_key = key.encode('utf-8')
    cipher = DES.new(des_key, DES.MODE_ECB)
    
    # Convert hex back to bytes
    encrypted_bytes = bytes.fromhex(hex_ciphertext)
    decrypted_padded = cipher.decrypt(encrypted_bytes)
    
    # Remove padding and decode to string
    return unpad(decrypted_padded, DES.block_size).decode('utf-8')

def main():
    while True:
        print("\n--- DES Encryption Menu ---")
        print("1. Encryption")
        print("2. Decryption")
        print("3. Exit")
        
        choice = input("Select an option: ")
        
        if choice == '3':
            print("Exiting...")
            break
            
        if choice in ['1', '2']:
            # DES keys MUST be exactly 8 characters
            key = input("Enter an 8-character key: ")
            if len(key) != 8:
                print("Error: Key must be exactly 8 characters.")
                continue
                
            if choice == '1':
                msg = input("Enter plaintext: ")
                print(f"Ciphertext (Hex): {encrypt_des(msg, key)}")
            else:
                hex_msg = input("Enter hex ciphertext: ")
                try:
                    print(f"Plaintext: {decrypt_des(hex_msg, key)}")
                except Exception:
                    print("Decryption failed. Ensure the key and ciphertext are correct.")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()