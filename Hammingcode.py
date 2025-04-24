def calculate_parity_bits(m):
    r = 0
    while (2 ** r) < (m + r + 1):
        r += 1
    return r

def generate_hamming_code(data_bits):
    m = len(data_bits)
    r = calculate_parity_bits(m)
    total_bits = m + r

    # Create a list with placeholders for parity bits
    hamming_code = [0] * total_bits
    j = 0

    # Place data bits and leave parity bits at 1, 2, 4, 8,...
    for i in range(1, total_bits + 1):
        if (i & (i - 1)) == 0:
            continue  # Skip positions that are powers of 2 (parity bits)
        hamming_code[i - 1] = data_bits[j]
        j += 1

    # Calculate parity bits
    for i in range(r):
        pos = 2 ** i
        parity = 0
        for j in range(1, total_bits + 1):
            if j & pos:
                parity ^= hamming_code[j - 1]
        hamming_code[pos - 1] = parity

    return hamming_code, r

def detect_and_correct(hamming_code):
    total_bits = len(hamming_code)
    r = calculate_parity_bits(total_bits - r)  # recalculate r
    error_pos = 0

    # Recalculate parity bits to find error position
    for i in range(r):
        pos = 2 ** i
        parity = 0
        for j in range(1, total_bits + 1):
            if j & pos:
                parity ^= hamming_code[j - 1]
        if parity != 0:
            error_pos += pos

    if error_pos == 0:
        print("✅ No error detected in the received code.")
    else:
        print(f"❌ Error detected at position: {error_pos}")
        # Correct the error
        hamming_code[error_pos - 1] ^= 1
        print("✅ Corrected Hamming code:", hamming_code)

    return hamming_code

# ---- MAIN PROGRAM ----
if __name__ == "__main__":
    data_input = input("Enter data bits (space-separated): ")
    data_bits = list(map(int, data_input.strip().split()))

    hamming_code, r = generate_hamming_code(data_bits)
    print("Generated Hamming Code:", hamming_code)

    received_input = input("Enter received code (space-separated, possibly with error): ")
    received_code = list(map(int, received_input.strip().split()))

    corrected_code = detect_and_correct(received_code)
