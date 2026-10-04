import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    # Store the position of each value
    pos = [0] * (n + 1)

    for i in range(n):
        pos[a[i]] = i

    possible = True

    # Consecutive values in sorted order
    # must be at positions of different parity.
    for x in range(1, n):
        if pos[x] % 2 == pos[x + 1] % 2:
            possible = False
            break

    print("YES" if possible else "NO")