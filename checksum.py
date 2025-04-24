def calculate_checksum(data):
    """
    Function to calculate the checksum by summing the byte values
    and taking modulo 256 to keep it within 1 byte.
    """
    checksum = 0
    for byte in data:
        checksum += byte  # Sum each byte value
    checksum = checksum % 256  # Ensure checksum is within 1 byte (0-255)
    return checksum

def main():
    # Example input data (could be any binary data or byte values)
    data = [72, 101, 108, 108, 111]  # "Hello" in ASCII byte values
    
    # Calculate checksum
    checksum = calculate_checksum(data)
    
    print("Data:", data)
    print("Checksum:", checksum)

    # Verify checksum by adding it to the data and checking sum
    # Simulating data transmission with checksum
    transmitted_data = data + [checksum]  # Attach checksum to the end of the data
    print("Transmitted Data with Checksum:", transmitted_data)

    # Validate checksum
    received_data = transmitted_data[:-1]  # Remove the checksum for validation
    received_checksum = transmitted_data[-1]  # Extract the received checksum
    calculated_checksum = calculate_checksum(received_data)

    if calculated_checksum == received_checksum:
        print("Checksum verified: No error detected")
    else:
        print("Checksum mismatch: Error detected")

if __name__ == "__main__":
    main()
