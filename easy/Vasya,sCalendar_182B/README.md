Here’s a clean **README.md** with the Python 3 solution:

# B. Vasya's Calendar

## Problem

Vasya lives in a strange world where a year has `n` months, and the `i`-th month contains `a[i]` days.

His clock displays only the **day number**, from `1` to `d`, and does not know which month it is.

Whenever the displayed day does not match the actual day, Vasya manually increases the clock's day number until it becomes correct.

Initially, on the first day of the first month, the clock shows `1`.

The task is to calculate the total number of manual increases Vasya performs during the entire year.

## Key Observation

We only need to consider the **first day of each month after the first month**.

Suppose a month has `a[i]` days.

At the end of that month, the clock automatically moves to the next number:

* If `a[i] < d`, it becomes `a[i] + 1`.
* If `a[i] = d`, it wraps around to `1`.

The actual day on the first day of the next month is always `1`.

### Case 1: `a[i] = d`

The clock already shows `1`, so Vasya performs:

```text
0 operations
```

### Case 2: `a[i] < d`

The clock shows `a[i] + 1`.

Vasya needs to increase it until it wraps around to `1`.

The number of required operations is:

```text
d - a[i]
```

Therefore, for every month except the last one, we add:

```text
d - a[i]
```

to the answer.

## Algorithm

1. Read `d`, the maximum day number on the clock.
2. Read `n`, the number of months.
3. Read the number of days in each month.
4. For every month except the last:

   * Add `d - a[i]` to the answer.
5. Print the answer.

## Python 3 Solution

```python
d = int(input())
n = int(input())

a = list(map(int, input().split()))

ans = 0

for i in range(n - 1):
    ans += d - a[i]

print(ans)
```

## Example

### Input

```text
5
3
3 4 3
```

### Calculation

For the first month:

```text
5 - 3 = 2
```

For the second month:

```text
5 - 4 = 1
```

Total:

```text
2 + 1 = 3
```

### Output

```text
3
```

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)` because the month lengths are stored in a list.

The calculation itself can also be implemented with `O(1)` extra space by processing the month lengths as they are read.
