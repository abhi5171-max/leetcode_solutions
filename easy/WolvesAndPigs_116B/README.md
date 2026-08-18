# B. Little Pigs and Wolves — README

## Problem

You are given an `n × m` grid containing:

* `P` — a little pig
* `W` — a wolf
* `.` — an empty cell

A pig and a wolf are adjacent if their cells share a side.

It is guaranteed that **each pig has at most one adjacent wolf**.

Each wolf can eat **at most one pig**, and a pig can be eaten only once.

The goal is to find the **maximum number of pigs that can be eaten**.

---

## Approach

Because every pig is adjacent to **at most one wolf**, there is no conflict where two wolves compete for the same pig.

Therefore, we can simply check every wolf and see whether it has an adjacent pig.

For each cell containing `W`:

1. Check its four possible neighboring cells:

   * Up
   * Down
   * Left
   * Right
2. If any neighboring cell contains `P`, this wolf can eat that pig.
3. Increment the answer.
4. Move to the next wolf.

Since every pig has at most one adjacent wolf, counting such wolf-pig pairs gives the maximum possible number of eaten pigs.

### Complexity

There are at most `n × m` cells, and each cell checks at most 4 neighbors.

* **Time:** `O(n × m)`
* **Space:** `O(n × m)` for storing the grid

With `n, m ≤ 10`, this is easily within the limits.

---

## Python 3 Solution

```python
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
```

---

## Example

### Input

```text
2 3
PPW
W.P
```

Grid:

```text
P P W
W . P
```

* The wolf at `(0, 2)` can eat the pig at `(0, 1)`.
* The wolf at `(1, 0)` can eat the pig at `(0, 0)`.

Therefore:

```text
2
```

### Output

```text
2
```

---

## Key Idea

> **For every wolf, find whether it has an adjacent pig.**

The important condition is that **a pig has at most one adjacent wolf**, which means we don't need complicated matching or graph algorithms. Each wolf can independently choose its adjacent pig.

---

## Topics

* 2D Grid
* Matrix Traversal
* Simulation
* Directional Neighbors
* Greedy Approach
* Implementation

**Codeforces:** B. Little Pigs and Wolves
