n, m = map(int, input().split())

grid = [input().strip() for _ in range(n)]

directions = [
    (-1, 0),  # Up
    (1, 0),   # Down
    (0, -1),  # Left
    (0, 1)    # Right
]

ans = 0

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'W':
            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if 0 <= ni < n and 0 <= nj < m:
                    if grid[ni][nj] == 'P':
                        ans += 1
                        break

print(ans)