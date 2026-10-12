
t = int(input())

for _ in range(t):
    l, a, b = map(int, input().split())

    pos = a
    ans = a

    for _ in range(l):
        pos = (pos + b) % l
        ans = max(ans, pos)

    print(ans)
