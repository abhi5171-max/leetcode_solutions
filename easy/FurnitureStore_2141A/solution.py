
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    mn = a[0]
    ans = []

    for i in range(1, n):
        if a[i] > mn:
            ans.append(i + 1)
        else:
            mn = a[i]

    print(len(ans))
    if ans:
        print(*ans)
    else:
        print()
