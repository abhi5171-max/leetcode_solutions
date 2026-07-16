n = int(input())
a = list(map(int, input().split()))

min_diff = abs(a[-1] - a[0])
x, y = n, 1

for i in range(n - 1):
    diff = abs(a[i] - a[i + 1])
    if diff < min_diff:
        min_diff = diff
        x, y = i + 1, i + 2

print(x, y)