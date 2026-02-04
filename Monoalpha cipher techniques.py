ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def encrypt(text, key):
    result = ""
    for char in text:
        if char.upper() in ALPHABET:
            # Step 1: Find where the letter sits in the normal alphabet
            index = ALPHABET.find(char.upper())
            # Step 2: Swap it with the letter at that same spot in the scrambled key
            new_char = key[index]
            result += new_char if char.isupper() else new_char.lower()
        else:
            result += char
    return result

def decrypt(text, key):
    result = ""
    for char in text:
        if char.upper() in key:
            # Step 1: Find where the letter sits in the scrambled key
            index = key.find(char.upper())
            # Step 2: Swap it back to the normal alphabet
            new_char = ALPHABET[index]
            result += new_char if char.isupper() else new_char.lower()
        else:
            result += char
    return result

def main():
    # This is a keyboard-layout scrambled alphabet
    cipher_key = "QWERTYUIOPASDFGHJKLZXCVBNM"
    
    while True:
        print("\n--- Monoalphabetic Cipher ---")
        print(f"Key: {cipher_key}")
        choice = input("1. Encrypt\n2. Decrypt\n3. Exit\nSelect: ")
        
        if choice == '1':
            msg = input("Enter plaintext: ")
            print(f"Result: {encrypt(msg, cipher_key)}")
        elif choice == '2':
            msg = input("Enter ciphertext: ")
            print(f"Result: {decrypt(msg, cipher_key)}")
        elif choice == '3':
            break

if __name__ == "__main__":
    main()