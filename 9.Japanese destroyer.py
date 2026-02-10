def create_matrix(key):
    # Standardize the key: uppercase, replace J with I, and remove spaces
    key = key.upper().replace("J", "I").replace(" ", "")
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
    matrix = []
    seen = set()
    
    # Build the 5x5 matrix
    for char in key + alphabet:
        if char not in seen:
            seen.add(char)
            matrix.append(char)
    return [matrix[i:i+5] for i in range(0, 25, 5)]

def find_pos(matrix, char):
    for r, row in enumerate(matrix):
        if char in row: 
            return r, row.index(char)
    return None

def decrypt_playfair(ciphertext, key):
    matrix = create_matrix(key)
    
    # IMPORTANT: Ciphertext must also replace J with I to match the matrix
    ciphertext = ciphertext.upper().replace(" ", "").replace("J", "I")
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        # The crash was happening here because 'J' wasn't in the matrix
        pos1 = find_pos(matrix, ciphertext[i])
        pos2 = find_pos(matrix, ciphertext[i+1])
        
        r1, c1 = pos1
        r2, c2 = pos2
        
        if r1 == r2: # Same row: shift left
            plaintext += matrix[r1][(c1-1)%5] + matrix[r2][(c2-1)%5]
        elif c1 == c2: # Same column: shift up
            plaintext += matrix[(r1-1)%5][c1] + matrix[(r2-1)%5][c2]
        else: # Rectangle: swap columns
            plaintext += matrix[r1][c2] + matrix[r2][c1]
            
    return plaintext

# --- Execution ---
cipher = "KXJEYUREBEZWEHEWRYTUHEYFSKREHEGOYFIWTTTUOLKSYCAJPOBOTEIZONTXBYBNTGONEYCUZWRGDSONSXBOUYWRHEBAAHYUSEDQ"
key = "ROYAL NEW ZEALAND NAVY"

decrypted = decrypt_playfair(cipher, key)

print("--- PT-109 Decoder ---")
print(f"Key: {key}")
print(f"Decrypted Message:\n{decrypted}")