t = int(input())

for _ in range(t):
    n, k, x = map(int, input().split())
    a = map(int, input().split())

    total = sum(a)

    if total <= k and (k - total) % x == 0:
        print("YES")
    else:
        print("NO")