n, k = map(int, input().split())
a = list(map(int, input().split()))

x = a[k - 1]

# Every element from position k to n
# must already be equal to a[k-1].
for i in range(k - 1, n):
    if a[i] != x:
        print(-1)
        break
else:
    # Count elements before position k
    # that are different from x.
    ans = 0

    for i in range(k - 1):
        if a[i] != x:
            ans += 1

    print(ans)