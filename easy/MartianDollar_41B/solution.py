n, b = map(int, input().split())
prices = list(map(int, input().split()))

ans = b

for i in range(n):
    dollars = b // prices[i]
    remaining = b % prices[i]

    for j in range(i + 1, n):
        money = remaining + dollars * prices[j]
        ans = max(ans, money)

print(ans)