# PC-2 Table (used to select 48 bits from the 56-bit key)
PC2 = (
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
)

# Right shift schedule for DECRYPTION
# We start with 0 because K16 uses the C/D state as it is after the final encryption shift
REV_SHIFT_SCHEDULE = [0, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

def right_shift(bits, n):
    return bits[-n:] + bits[:-n] if n > 0 else bits

def generate_decryption_keys(initial_56bit_key):
    # Split key into C and D
    C = initial_56bit_key[:28]
    D = initial_56bit_key[28:]
    
    # To get to the starting point of K16, we must first 
    # perform all 16 left shifts used in encryption.
    encryption_shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    for s in encryption_shifts:
        C = (C[s:] + C[:s])
        D = (D[s:] + D[:s])
    
    print("--- Generating Decryption Subkeys (K16 down to K1) ---")
    
    for round_num, s in enumerate(REV_SHIFT_SCHEDULE):
        # Shift Right
        C = right_shift(C, s)
        D = right_shift(D, s)
        
        # Apply PC-2
        combined = C + D
        subkey = "".join(combined[i-1] for i in PC2)
        
        # In decryption, Round 1 uses K16, Round 2 uses K15...
        print(f"Round {round_num+1:2} Key (K{16-round_num:02}): {subkey[:20]}...")

# Example 56-bit key
key_56 = "1010101011110000110011001010" + "0000111100110011101010101111"
generate_decryption_keys(key_56)