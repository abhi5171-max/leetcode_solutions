
t = int(input())

for _ in range(t):
    n, c = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)

    free = 0

    for weight in a:
        if weight * (2 ** free) <= c:
            free += 1

    print(n - free)
