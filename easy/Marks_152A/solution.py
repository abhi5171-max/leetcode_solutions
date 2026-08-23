n, m = map(int, input().split())

marks = [input().strip() for _ in range(n)]

successful = set()

for j in range(m):
    maximum = max(marks[i][j] for i in range(n))

    for i in range(n):
        if marks[i][j] == maximum:
            successful.add(i)

print(len(successful))