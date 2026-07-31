board = [input().strip() for _ in range(8)]

full_rows = 0

for row in board:
    if row == "B" * 8:
        full_rows += 1

if full_rows == 8:
    print(8)
else:
    cols = 0
    for j in range(8):
        needed = False
        for i in range(8):
            if board[i] != "B" * 8 and board[i][j] == 'B':
                needed = True
                break
        if needed:
            cols += 1

    print(full_rows + cols)