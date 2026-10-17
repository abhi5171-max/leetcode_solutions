t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    max_so_far = a[0]
    ans = 0

    for i in range(1, n):
        if a[i] < max_so_far:
            ans += 1
        else:
            max_so_far = a[i]

    print(ans)