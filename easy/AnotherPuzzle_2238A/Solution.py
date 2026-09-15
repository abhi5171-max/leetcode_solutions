import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, c = map(int, input().split())

    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    INF = 10**18
    answer = INF

    # Case 1: No reordering
    possible = True
    cost = 0

    for i in range(n):
        if a[i] < b[i]:
            possible = False
            break
        cost += a[i] - b[i]

    if possible:
        answer = min(answer, cost)

    # Case 2: Reorder once
    a.sort()
    b.sort()

    possible = True
    cost = c

    for i in range(n):
        if a[i] < b[i]:
            possible = False
            break
        cost += a[i] - b[i]

    if possible:
        answer = min(answer, cost)

    if answer == INF:
        print(-1)
    else:
        print(answer)
