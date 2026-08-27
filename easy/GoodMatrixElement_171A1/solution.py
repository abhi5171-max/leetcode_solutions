n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

mid = n // 2
total = 0

for i in range(n):
    for j in range(n):
        if (
            i == j
            or i + j == n - 1
            or i == mid
            or j == mid
        ):
            total += matrix[i][j]

print(total)