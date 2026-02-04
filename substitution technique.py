def text_to_numbers(text):
    result = []
    for char in text.upper():
        if char.isalpha():
            # ord('A') is 65. So 65 - 65 + 1 = 1 (A=1)
            number = ord(char) - ord('A') + 1
            result.append(str(number))
        else:
            result.append(char)
    return " ".join(result)

def numbers_to_text(numeric_string):
    result = ""
    # split() looks for spaces between the numbers
    parts = numeric_string.split()
    for part in parts:
        if part.isdigit():
            # 1 + 65 - 1 = 65 ('A')
            char = chr(int(part) + ord('A') - 1)
            result += char
        else:
            result += part
    return result

def main():
    while True:
        print("\n--- Numeric Substitution Menu ---")
        print("1. Encryption (Text to Numbers)")
        print("2. Decryption (Numbers to Text)")
        print("3. Exit")
        
        choice = input("Select an option (1-3): ")
        
        if choice == '1':
            msg = input("Enter text: ")
            print(f"Output: {text_to_numbers(msg)}")
        elif choice == '2':
            msg = input("Enter numbers (separated by spaces): ")
            print(f"Output: {numbers_to_text(msg)}")
        elif choice == '3':
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()