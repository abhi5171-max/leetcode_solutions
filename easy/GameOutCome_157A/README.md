# A. Game Outcome — README

## Problem

You are given an `n × n` board where every cell contains an integer.

For each cell `(i, j)`:

* Calculate the **sum of all numbers in its row**.
* Calculate the **sum of all numbers in its column**.
* The cell is **winning** if:

```text
column_sum > row_sum
```

Your task is to count the total number of winning cells.

---

## Approach

Instead of calculating the row and column sums repeatedly for every cell, calculate them once.

### Step 1: Calculate row sums

For every row `i`:

```text
row_sum[i] = sum of all elements in row i
```

### Step 2: Calculate column sums

For every column `j`:

```text
col_sum[j] = sum of all elements in column j
```

### Step 3: Check every cell

For each cell `(i, j)`:

```text
if col_sum[j] > row_sum[i]:
    answer += 1
```

The important point is that the cell itself is included in **both** sums, exactly as required by the problem.

---

## Example

Consider:

```text
1 2
3 4
```

### Row sums

```text
Row 1 = 1 + 2 = 3
Row 2 = 3 + 4 = 7
```

### Column sums

```text
Column 1 = 1 + 3 = 4
Column 2 = 2 + 4 = 6
```

Now check each cell:

```text
(1,1): column 4 > row 3 → winning
(1,2): column 6 > row 3 → winning
(2,1): column 4 > row 7 → not winning
(2,2): column 6 > row 7 → not winning
```

Therefore:

```text
Answer = 2
```

---

## Python 3 Solution

```python
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
```

---

## Complexity

There are `n²` cells.

### Time Complexity

```text
O(n²)
```

We traverse the board a constant number of times.

### Space Complexity

```text
O(n²)
```

because we store the board.

The constraints are only `n ≤ 30`, so this easily fits within the limits.

---

## Key Idea

The main optimization is to **precompute row sums and column sums**.

Instead of doing:

```text
for every cell:
    calculate its entire row sum
    calculate its entire column sum
```

we calculate each row and column sum only once:

```text
row_sum[i]
col_sum[j]
```

Then checking a cell becomes simply:

```python
if col_sum[j] > row_sum[i]:
    answer += 1
```

### Final Condition

```text
Winning cell ⇔ column_sum[j] > row_sum[i]
```

**Important:** The comparison is **strictly greater (`>`)**, not greater than or equal to (`>=`).
