# Good Matrix Elements

## Problem Statement

Given an odd-sized `n × n` matrix, an element is considered **good** if it belongs to at least one of these:

* Main diagonal: `i == j`
* Secondary diagonal: `i + j == n - 1`
* Middle row: `i == n // 2`
* Middle column: `j == n // 2`

The task is to calculate the **sum of all good elements**.

> Since some elements belong to more than one of these lines, each good element must be counted **only once**.

---

## Approach

For every element `a[i][j]`, check whether it satisfies any of the four conditions:

```text
i == j
i + j == n - 1
i == n // 2
j == n // 2
```

If at least one condition is true, add the element to the answer.

### Why this works

These four conditions exactly represent the:

* Main diagonal
* Secondary diagonal
* Middle row
* Middle column

Using `or` ensures that an element lying on multiple lines is still added only once.

---

## Python Implementation

```python
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
```

---

## Example 1

### Input

```text
3
1 2 3
4 5 6
7 8 9
```

For a `3 × 3` matrix, all elements belong to at least one of the four required lines.

Therefore:

```text
1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 = 45
```

### Output

```text
45
```

---

## Example 2

### Input

```text
5
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
1 1 1 1 1
```

There are `17` unique good positions in a `5 × 5` matrix.

Since every value is `1`, the sum is:

```text
17 × 1 = 17
```

### Output

```text
17
```

---

## Complexity

There are `n²` elements, and each element is checked once.

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(n²)` for storing the matrix

With `n ≤ 101`, this easily fits within the limits.

## Key Takeaway

The simplest solution is to **check each matrix position against the four conditions** and add it if it lies on any good line.
