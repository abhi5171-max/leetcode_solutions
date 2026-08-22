n = int(input())
a = list(map(int, input().split()))

seen = [False] * (n + 1)
changes = 0

for x in a:
    if 1 <= x <= n:
        if seen[x]:
            changes += 1
        else:
            seen[x] = True
    else:
        changes += 1

print(changes)