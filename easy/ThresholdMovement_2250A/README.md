# Threshold Movement

## Problem

There are `n` positions numbered from `1` to `n`. Initially, position `i` contains an element with weight `a[i]`.

You choose an integer `x`. Every element moves simultaneously:

* If `a[i] < x`, it moves to position `i + 1`.
* If `a[i] > x`, it moves to position `i - 1`.
* If `a[i] = x`, the movement fails.

An integer `x` is **perfect** if:

1. No element causes the movement to fail.
2. After all movements, every position contains exactly one element.

Determine whether a perfect integer `x` exists.

## Key Observation

For every position to be occupied exactly once, the movement directions must alternate.

Thus, the weights must alternate around `x`:

```text
a[0] < x, a[1] > x, a[2] < x, ...
```

or

```text
a[0] > x, a[1] < x, a[2] > x, ...
```

For a particular pattern, maintain:

* `low` = maximum value that must be smaller than `x`
* `high` = minimum value that must be greater than `x`

A valid integer exists when:

```text
low < x < high
```

Since `x` must be an integer, this is equivalent to:

```text
low + 1 < high
```

We check both possible alternating patterns.

## Python Solution

```python
import sys


def possible(a, first_less):
    low = -10**30
    high = 10**30

    for i, value in enumerate(a):
        if i % 2 == 0:
            less = first_less
        else:
            less = not first_less

        if less:
            low = max(low, value)
        else:
            high = min(high, value)

    return low + 1 < high


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        if possible(a, True) or possible(a, False):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    solve()
```

## Example

### Input

```text
6
1
7
2
3 1
2
2 1
4
9 1 7 2
4
9 8 7 1
6
1000000000 1 9 2 8 3
```

### Output

```text
NO
YES
NO
YES
NO
YES
```

## Complexity

For each test case:

* **Time:** `O(n)`
* **Space:** `O(n)` for storing the array.

The algorithm performs only two linear scans conceptually, so it is efficient for large input sizes.

## Tags

`Codeforces` `Greedy` `Arrays` `Implementation` `Math` `Python`
