
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    ans = 1 + sum(max(0, a[i] - b[i]) for i in range(n))

    print(ans)
