
t = int(input())

for _ in range(t):
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))

    # Loss if a bank is used as a source
    loss = [(v // x) * (x - y) + (v % x) for v in a]

    # Keep the bank with the maximum loss as the destination
    idx = loss.index(max(loss))

    ans = a[idx]

    for i in range(n):
        if i != idx:
            ans += (a[i] // x) * y

    print(ans)
