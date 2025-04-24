def perform_xor(temp, generator, data_len, gen_len):
    for i in range(data_len):
        if temp[i] == 1:
            for j in range(gen_len):
                temp[i + j] ^= generator[j]

def main():
    data_len = int(input("Enter the number of bits in data: "))
    data_bits = list(map(int, input(f"Enter {data_len} data bits: ").split()))

    gen_len = int(input("Enter number of bits in generator: "))
    generator = list(map(int, input(f"Enter {gen_len} generator bits: ").split()))

    # Append zeros to data bits for CRC calculation
    temp = data_bits + [0] * (gen_len - 1)

    perform_xor(temp, generator, data_len, gen_len)

    crc = temp[data_len:]
    print("CRC bits:", crc)

    transmitted = data_bits + crc
    print("Transmitted data:", transmitted)

    received = list(map(int, input(f"Enter received {len(transmitted)} bits: ").split()))

    perform_xor(received, generator, data_len, gen_len)

    if all(bit == 0 for bit in received[data_len:]):
        print("No error")
    else:
        print("Error detected")

if __name__ == "__main__":
    main()
