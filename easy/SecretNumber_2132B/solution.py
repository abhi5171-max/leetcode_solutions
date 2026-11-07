t = int(input())

for _ in range(t):
    n = int(input())
    ans = []

    p = 10

    while p + 1 <= n:
        if n % (p + 1) == 0:
            ans.append(n // (p + 1))

        p *= 10

    ans.sort()

    print(len(ans), *ans)