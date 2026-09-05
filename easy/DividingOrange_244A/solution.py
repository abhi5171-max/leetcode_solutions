n, k = map(int, input().split())
a = list(map(int, input().split()))

children = [(a[i], i) for i in range(k)]
children.sort(reverse=True)

requested = set(a)

used = [False] * (n * k + 1)
ans = [[] for _ in range(k)]

current = n * k

for value, child in children:
    # Give requested segment
    ans[child].append(value)
    used[value] = True

    # Give remaining n-1 segments
    while len(ans[child]) < n:
        while used[current] or current in requested:
            current -= 1

        ans[child].append(current)
        used[current] = True
        current -= 1

for child in range(k):
    print(*ans[child])