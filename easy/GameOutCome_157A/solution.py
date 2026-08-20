n = int(input())

board = []

for _ in range(n):
    board.append(list(map(int, input().split())))

# Calculate row sums
row_sum = [sum(row) for row in board]

# Calculate column sums
col_sum = [0] * n

for i in range(n):
    for j in range(n):
        col_sum[j] += board[i][j]

# Count winning cells
answer = 0

for i in range(n):
    for j in range(n):
        if col_sum[j] > row_sum[i]:
            answer += 1

print(answer)