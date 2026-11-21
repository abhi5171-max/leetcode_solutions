
t = int(input())

for _ in range(t):
    x = int(input())

    a = [0, 0, 0]
    ans = 0

    while a[0] < x:
        a[0] = min(x, 2 * a[1] + 1)

        a.sort()

        ans += 1

    print(ans)
