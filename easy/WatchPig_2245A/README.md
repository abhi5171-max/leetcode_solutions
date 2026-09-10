# A. Who Watches the Watchpig?

## Problem Summary

There are `n` piggies standing in a line. Each piggy faces either:

* `R` — Right
* `L` — Left

Two piggies `(x, y)` form a **watchpig pair** if:

* `x < y`
* Piggy `x` faces `R`
* Piggy `y` faces `L`

A piggy is called **safe** if it belongs to at least `k` watchpig pairs.

We can flip the direction of any piggy. The goal is to find the **minimum number of flips** required to make every piggy safe.

If it is impossible, output `-1`.

---

## Key Observation

For a piggy facing `L` at position `i` to belong to at least `k` watchpig pairs, there must be at least `k` piggies facing `R` before it.

Therefore, the **first `k` piggies must all face `R`**.

Similarly, for a piggy facing `R` to belong to at least `k` watchpig pairs, there must be at least `k` piggies facing `L` after it.

Therefore, the **last `k` piggies must all face `L`**.

The piggies in between can face either direction.

---

## Impossible Case

The first `k` positions must be `R` and the last `k` positions must be `L`.

If these two sections overlap:

```text
2 × k > n
```

then it is impossible to satisfy both conditions.

So the answer is:

```text
If 2 * k > n → -1
```

Otherwise:

* Count `L` in the first `k` positions.
* Count `R` in the last `k` positions.

The total count is the minimum number of flips.

---

## Algorithm

For each test case:

1. Check if `2 * k > n`.

   * If yes, print `-1`.
2. Count `L` characters in the first `k` positions.
3. Count `R` characters in the last `k` positions.
4. Print the total number of required flips.

---

## Python 3 Solution

```python
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    # Impossible if the required sections overlap
    if 2 * k > n:
        print(-1)
        continue

    flips = 0

    # First k piggies must face Right
    for i in range(k):
        if s[i] == 'L':
            flips += 1

    # Last k piggies must face Left
    for i in range(n - k, n):
        if s[i] == 'R':
            flips += 1

    print(flips)
```

---

## Complexity

* **Time Complexity:** `O(n)` per test case
* **Space Complexity:** `O(1)`

---

## Example

### Input

```text
4
3 1
LLL
4 3
LRLR
6 2
RLLRRL
12 4
LRLLRRLRLRLR
```

### Output

```text
1
-1
2
5
```
