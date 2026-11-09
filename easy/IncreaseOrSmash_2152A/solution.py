t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    distinct = len(set(a))

    ans = 2 * distinct - 1

    print(ans)