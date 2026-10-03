t = int(input())

for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))

    # Store the position of each value
    pos = [0] * (n + 1)

    for i in range(n):
        pos[p[i]] = i

    # Find the first incorrect position
    l = -1

    for i in range(n):
        expected = n - i

        if p[i] != expected:
            l = i
            break

    # If an improvement is possible
    if l != -1:
        r = pos[n - l]

        # Reverse p[l...r]
        p[l:r + 1] = p[l:r + 1][::-1]

    print(*p)