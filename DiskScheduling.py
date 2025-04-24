def fcfs(requests, head):
    """🔁 First-Come-First-Serve (FCFS):
    Process requests in the order they arrive."""
    seek = 0
    print("FCFS Order:", end=" ")
    for req in requests:
        print(req, end=" ")
        seek += abs(head - req)
        head = req
    print(f"\nTotal seek operations: {seek}\n")


def sstf(requests, head):
    """🧠 Shortest Seek Time First (SSTF):
    Always serve the nearest request to current head position."""
    pending = requests[:]
    seek = 0
    print("SSTF Order:", end=" ")
    while pending:
        next_req = min(pending, key=lambda r: abs(r - head))
        print(next_req, end=" ")
        seek += abs(head - next_req)
        head = next_req
        pending.remove(next_req)
    print(f"\nTotal seek operations: {seek}\n")


def scan(requests, head, disk_size, direction_right=True):
    """🚀 SCAN (Elevator Algorithm):
    Head moves in one direction fulfilling requests until end, then reverses."""
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
    left.sort()
    right.sort()
    order = []

    if direction_right:
        order += right + [disk_size - 1] + left[::-1]
    else:
        order += left[::-1] + [0] + right

    seek = 0
    print("SCAN Order:", end=" ")
    for req in order:
        print(req, end=" ")
        seek += abs(head - req)
        head = req
    print(f"\nTotal seek operations: {seek}\n")


def cscan(requests, head, disk_size, direction_right=True):
    """🔄 C-SCAN (Circular SCAN):
    Like SCAN, but after reaching the end, head jumps to the opposite end and continues."""
    left = [r for r in requests if r < head]
    right = [r for r in requests if r >= head]
    left.sort()
    right.sort()
    order = []

    if direction_right:
        order += right + [disk_size - 1, 0] + left
    else:
        order += left[::-1] + [0, disk_size - 1] + right[::-1]

    seek = 0
    print("C-SCAN Order:", end=" ")
    for req in order:
        print(req, end=" ")
        seek += abs(head - req)
        head = req
    print(f"\nTotal seek operations: {seek}\n")


def look(requests, head, direction_right=True):
    """👀 LOOK:
    Like SCAN but only goes as far as the last request in each direction (doesn’t go to end)."""
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])
    order = right + left[::-1] if direction_right else left[::-1] + right

    seek = 0
    print("LOOK Order:", end=" ")
    for req in order:
        print(req, end=" ")
        seek += abs(head - req)
        head = req
    print(f"\nTotal seek operations: {seek}\n")


def clook(requests, head, direction_right=True):
    """🔁 C-LOOK:
    Like LOOK, but jumps back to beginning instead of reversing."""
    left = sorted([r for r in requests if r < head])
    right = sorted([r for r in requests if r >= head])
    order = right + left if direction_right else left[::-1] + right[::-1]

    seek = 0
    print("C-LOOK Order:", end=" ")
    for req in order:
        print(req, end=" ")
        seek += abs(head - req)
        head = req
    print(f"\nTotal seek operations: {seek}\n")
def main():
    requests = list(map(int, input("Enter disk requests: ").split()))
    head = int(input("Enter initial head position: "))
    disk_size = int(input("Enter disk size: "))
    direction = int(input("Direction (0: left, 1: right): "))
    right = direction == 1

    print("\n--- Disk Scheduling Simulation ---\n")
    fcfs(requests, head)
    sstf(requests, head)
    scan(requests, head, disk_size, right)
    cscan(requests, head, disk_size, right)
    look(requests, head, right)
    clook(requests, head, right)

if __name__ == "__main__":
    main()

