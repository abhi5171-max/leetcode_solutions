n, m, s = map(int, input().split())

# Number of row positions belonging to the largest residue classes
q_row, r_row = divmod(n, s)
if r_row == 0:
    best_rows = n
else:
    best_rows = r_row * (q_row + 1)

# Number of column positions belonging to the largest residue classes
q_col, r_col = divmod(m, s)
if r_col == 0:
    best_cols = m
else:
    best_cols = r_col * (q_col + 1)

print(best_rows * best_cols)