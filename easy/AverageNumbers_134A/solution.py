n = int(input())
a = list(map(int, input().split()))

total = sum(a)
ans = []

for i in range(n):
    if a[i] * n == total:
        ans.append(i + 1)

print(len(ans))

if ans:
    print(*ans)