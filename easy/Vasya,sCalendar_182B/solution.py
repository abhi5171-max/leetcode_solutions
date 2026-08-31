d = int(input())
n = int(input())

a = list(map(int, input().split()))

ans = 0

for i in range(n - 1):
    ans += d - a[i]

print(ans)