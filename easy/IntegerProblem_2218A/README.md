# A. The 67th Integer Problem

## Problem

You are given an integer `x`. Choose an integer `y` such that:

$$
\min(x,y)
$$

is maximized.

The constraints are:

* `-67 ≤ x ≤ 67`
* `-67 ≤ y ≤ 67`

If multiple values of `y` are possible, any valid one can be printed.

---

## Approach

Since `x` is fixed, the maximum possible value of:

$$
\min(x,y)
$$

is `x`.

To make `min(x, y) = x`, we need:

$$
y \ge x
$$

For every `x < 67`, we can simply choose:

```text
y = x + 1
```

For `x = 67`, `68` is outside the allowed range, so we choose:

```text
y = 67
```

Thus:

```text
if x < 67:
    y = x + 1
else:
    y = 67
```

---

## Algorithm

1. Read the number of test cases `t`.
2. For each test case, read `x`.
3. If `x < 67`, print `x + 1`.
4. Otherwise, print `67`.

---

## Python Implementation

```python
import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        x = int(input())

        if x < 67:
            print(x + 1)
        else:
            print(67)


if __name__ == "__main__":
    solve()
```

---

## Complexity

* **Time Complexity:** `O(t)`
* **Space Complexity:** `O(1)`

---

## Example

### Input

```text
3
1
3
5
```

### Output

```text
2
4
6
```

For example, when `x = 5`:

```text
y = 6

min(5, 6) = 5
```

Since `5` is the maximum possible value of `min(5, y)`, the answer is valid.
