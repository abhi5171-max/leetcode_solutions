n, x0 = map(int, input().split())

left = 0
right = 1000

for _ in range(n):
    a, b = map(int, input().split())
    l = min(a, b)
    r = max(a, b)
    left = max(left, l)
    right = min(right, r)

if left > right:
    print(-1)
else:
    if left <= x0 <= right:
        print(0)
    elif x0 < left:
        print(left - x0)
    else:
        print(x0 - right)