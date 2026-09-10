t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    # Impossible if the required sections overlap
    if 2 * k > n:
        print(-1)
        continue

    flips = 0

    # First k piggies must face Right
    for i in range(k):
        if s[i] == 'L':
            flips += 1

    # Last k piggies must face Left
    for i in range(n - k, n):
        if s[i] == 'R':
            flips += 1

    print(flips)