# A. Lawn Mower

## Problem Statement

You are given:

* `n` — number of fence boards.
* `m` — width of the lawn mower.

If **at least `m` consecutive boards** are removed, the lawn mower can pass through the hole and leave the territory.

Your task is to find the **maximum number of boards that can be removed** while ensuring that the lawn mower cannot escape.

### Constraints

* `1 ≤ n, m ≤ ...`
* Multiple test cases are given.

---

## Key Observation

We **cannot remove `m` consecutive boards**.

Therefore, after every `m - 1` removed boards, we need to keep at least **one board**.

For example, for:

```text
n = 9, m = 3
```

We can arrange the boards as:

```text
R R K R R K R R K
```

where:

* `R` = removed
* `K` = kept

We keep `3` boards, so:

```text
Removed = 9 - 3 = 6
```

The general formula is:

```text
maximum removed = n - floor(n / m)
```

### Why?

Every group of `m` boards requires at least one board to remain.

So the minimum number of boards that must remain is:

```text
n // m
```

Therefore:

```text
answer = n - (n // m)
```

---

## Algorithm

For each test case:

1. Read `n` and `m`.
2. Calculate `n // m`.
3. Subtract it from `n`.
4. Print the result.

---

## Python Solution

```python
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())

    ans = n - (n // m)

    print(ans)
```

---

## Example

### Input

```text
5
9 3
13 4
15 14
20 1
1000 42
```

### Output

```text
6
10
14
0
977
```

### Explanation

|  `n` | `m` | `n // m` | Maximum Removed |
| ---: | --: | -------: | --------------: |
|    9 |   3 |        3 |               6 |
|   13 |   4 |        3 |              10 |
|   15 |  14 |        1 |              14 |
|   20 |   1 |       20 |               0 |
| 1000 |  42 |       23 |             977 |

For `m = 1`, even **one removed board** creates a hole of width `1`, so no board can be removed.

---

## Complexity

* **Time:** `O(t)`
* **Space:** `O(1)`

## Key Formula

```text
answer = n - n // m
```

This is an **O(1) solution per test case**.
