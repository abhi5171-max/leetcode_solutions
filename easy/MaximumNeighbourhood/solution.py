
t = int(input())

for _ in range(t):
    n = int(input())
    ans = 0

    for i in range(n):
        for j in range(n):
            value = i * n + j + 1
            cost = value

            if i > 0:
                cost += (i - 1) * n + j + 1
            if i < n - 1:
                cost += (i + 1) * n + j + 1
            if j > 0:
                cost += i * n + j
            if j < n - 1:
                cost += i * n + j + 2

            ans = max(ans, cost)

    print(ans)
