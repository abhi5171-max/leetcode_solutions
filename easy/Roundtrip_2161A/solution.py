
t = int(input())

for _ in range(t):
    a, x, k, n = map(int, input().split())
    s = input().strip()

    ans = 0

    for c in s:
        if c == '1':
            ans += 1
            a = max(0, a - k)
        else:
            if a < x:
                ans += 1
                a = max(0, a - k)

    print(ans)
