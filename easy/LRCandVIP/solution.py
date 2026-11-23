
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mx = max(a)

    if a.count(mx) == n:
        print("No")
    else:
        print("Yes")

        ans = [2] * n
        ans[a.index(mx)] = 1

        print(*ans)
