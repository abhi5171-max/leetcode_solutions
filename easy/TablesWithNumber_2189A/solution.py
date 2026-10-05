t= int(input())

for _ in range(t):
    n, h, l = map(int, input().split())
    a = list(map(int, input().split()))

    rows = 0
    cols = 0

    for x in a:
        if x <= h:
            rows += 1

        if x <= l:
            cols += 1

    answer = min(rows, cols, n // 2)

    print(answer)