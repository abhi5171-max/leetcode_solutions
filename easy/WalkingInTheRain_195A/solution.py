n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(a[0])
else:
    ans = float('inf')

    for i in range(n - 1):
        ans = min(ans, max(a[i], a[i + 1]))

    print(ans)