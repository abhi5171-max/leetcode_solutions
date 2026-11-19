
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))

    first = a.index(1)
    last = n - 1 - a[::-1].index(1)

    if last - first + 1 <= k:
        print("YES")
    else:
        print("NO")
