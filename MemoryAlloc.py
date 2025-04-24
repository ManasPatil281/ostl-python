def first_fit(blocks, processes):
    print("\nFirst Fit Allocation:")
    block_status = blocks.copy()

    for i, p in enumerate(processes):
        allocated = False
        for j in range(len(block_status)):
            if block_status[j] >= p:
                print(f"Process {i} of size {p} allocated to block of size {blocks[j]}")
                block_status[j] -= p
                allocated = True
                break
        if not allocated:
            print(f"Process {i} of size {p} couldn't be allocated")

def best_fit(blocks, processes):
    print("\nBest Fit Allocation:")
    block_status = blocks.copy()

    for i, p in enumerate(processes):
        best_index = -1
        for j in range(len(block_status)):
            if block_status[j] >= p:
                if best_index == -1 or block_status[j] < block_status[best_index]:
                    best_index = j

        if best_index != -1:
            print(f"Process {i} of size {p} allocated to block of size {blocks[best_index]}")
            block_status[best_index] -= p
        else:
            print(f"Process {i} of size {p} couldn't be allocated")

def worst_fit(blocks, processes):
    print("\nWorst Fit Allocation:")
    block_status = blocks.copy()

    for i, p in enumerate(processes):
        worst_index = -1
        for j in range(len(block_status)):
            if block_status[j] >= p:
                if worst_index == -1 or block_status[j] > block_status[worst_index]:
                    worst_index = j

        if worst_index != -1:
            print(f"Process {i} of size {p} allocated to block of size {blocks[worst_index]}")
            block_status[worst_index] -= p
        else:
            print(f"Process {i} of size {p} couldn't be allocated")

# Input
memory_blocks = list(map(int, input("Enter sizes of memory blocks (space-separated): ").split()))
processes = list(map(int, input("Enter sizes of processes (space-separated): ").split()))

# Run algorithms
first_fit(memory_blocks, processes)
best_fit(memory_blocks, processes)
worst_fit(memory_blocks, processes)
