t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    x = a[0]
    ans = 0

    # Check starting blocks where the pattern
    # may cross into another block.
    for k in range(x, min(n, x + m - 2) + 1):
        block = k
        val = x
        match = True

        for j in range(m):
            if val != a[j]:
                match = False
                break

            if val == block:
                block += 1
                val = 1
            else:
                val += 1

        if match:
            ans += 1

    # Check blocks where the entire pattern
    # fits inside the same block.
    if all(a[i] == x + i for i in range(m)):
        ans += max(0, n - x - m + 2)

    print(ans)