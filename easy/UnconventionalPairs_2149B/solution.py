
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    ans = 0
    for i in range(0, n, 2):
        ans = max(ans, a[i + 1] - a[i])

    print(ans)
