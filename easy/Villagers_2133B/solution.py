t = int(input())

for _ in range(t):
    n = int(input())
    a = sorted(map(int, input().split()))

    if n % 2 == 0:
        ans = sum(a[1::2])
    else:
        ans = sum(a[0::2])

    print(ans)