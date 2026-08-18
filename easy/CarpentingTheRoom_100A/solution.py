n, k, a = map(int, input().split())

needed_per_side = (n + a - 1) // a
needed = needed_per_side * needed_per_side

if needed <= k:
    print("YES")
else:
    print("NO")