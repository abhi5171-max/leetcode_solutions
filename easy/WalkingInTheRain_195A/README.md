Here’s a clean **README.md** for the Codeforces problem **B. Walking in the Rain**:

# B. Walking in the Rain

## Problem Description

You are given a boulevard consisting of `n` tiles numbered from `1` to `n`.

The opposition starts at tile `1` and needs to reach tile `n`.

From tile `i`, you can move:

* To tile `i + 1`
* To tile `i + 2` (jump over one tile)

Each tile `i` gets destroyed after `a[i]` days of rain. On day `a[i]`, the tile is still usable, while on day `a[i] + 1`, it is destroyed.

The goal is to determine the **maximum number of days for which it is still possible to travel from tile `1` to tile `n`**.

---

## Approach

Since we can move at most **two tiles forward**, we cannot cross two consecutive destroyed tiles.

For every pair of adjacent tiles `(i, i+1)`, at least one of them must remain available.

Both tiles in a pair become destroyed after:

```text
max(a[i], a[i+1])
```

days.

Therefore, the walk becomes impossible at the earliest such point:

```text
answer = min(max(a[i], a[i+1]))
```

For `n = 1`, there is only one tile, so the answer is simply:

```text
a[0]
```

---

## Algorithm

1. Read `n` and the array `a`.
2. If `n == 1`, print `a[0]`.
3. Otherwise, examine every pair of adjacent tiles.
4. Calculate `max(a[i], a[i+1])`.
5. Keep the minimum of these values.
6. Print the result.

---

## Example

### Input

```text
4
10 3 5 10
```

### Calculation

```text
max(10, 3) = 10
max(3, 5)  = 5
max(5, 10) = 10
```

Therefore:

```text
min(10, 5, 10) = 5
```

### Output

```text
5
```

---

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)` for storing the input array.

---

## Implementation

```python
n = int(input())
a = list(map(int, input().split()))

if n == 1:
    print(a[0])
else:
    ans = float('inf')

    for i in range(n - 1):
        ans = min(ans, max(a[i], a[i + 1]))

    print(ans)
```

---

## Key Takeaway

Because the maximum jump length is **2**, two consecutive destroyed tiles create an uncrossable gap.

Hence:

```text
Answer = min(max(a[i], a[i+1]))
```

This gives an `O(n)` solution, which easily fits the constraints.
