# A. A Simple Sequence

## Problem

Given an integer `n`, construct a permutation:

```text
a1, a2, ..., an
```

containing every integer from `1` to `n` exactly once, such that:

```text
a1 mod a2 ≥ a2 mod a3 ≥ ... ≥ an-1 mod an
```

Any valid permutation can be used.

---

## Key Observation

A very simple construction works:

```text
n, n-1, n-2, ..., 2, 1
```

That is, simply print the numbers from `n` down to `1`.

### Why does it work?

Consider two consecutive elements:

```text
x, x - 1
```

Since:

```text
x = 1 × (x - 1) + 1
```

we get:

```text
x mod (x - 1) = 1
```

Therefore, for the descending permutation:

```text
n, n-1, n-2, ..., 2, 1
```

the remainders are:

```text
1, 1, 1, ..., 1, 0
```

because:

```text
2 mod 1 = 0
```

Hence:

```text
1 ≥ 1 ≥ 1 ≥ ... ≥ 1 ≥ 0
```

So the required condition is always satisfied.

---

## Example

For:

```text
n = 5
```

we construct:

```text
5 4 3 2 1
```

Calculate the remainders:

```text
5 mod 4 = 1
4 mod 3 = 1
3 mod 2 = 1
2 mod 1 = 0
```

Thus:

```text
1 ≥ 1 ≥ 1 ≥ 0
```

The condition is satisfied.

---

## Algorithm

For every test case:

1. Read `n`.
2. Print the integers from `n` down to `1`.

---

## Complexity

For each test case:

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)` apart from the output.

---

## Python Implementation

```python
import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        print(*range(n, 0, -1))


if __name__ == "__main__":
    solve()
```

---

## Key Takeaway

> **The descending permutation `n, n-1, ..., 1` always works because its consecutive modulo values are `1, 1, ..., 1, 0`, which are non-increasing.**
