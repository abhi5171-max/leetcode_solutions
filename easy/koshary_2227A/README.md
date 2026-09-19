# Codeforces – A. Koshary

## Problem

Yousef starts at `(0, 0)` and wants to reach `(x, y)`.

He can make:

* **Long step:** `(a, b) → (a+2, b)` or `(a, b) → (a, b+2)`
* **Short step:** `(a, b) → (a+1, b)` or `(a, b) → (a, b+1)`

He can use **at most one short step** during the entire journey.

The task is to determine whether Yousef can reach exactly `(x, y)`.

---

## Approach

A long step changes one coordinate by `2`, so it does not change the parity of that coordinate.

A short step changes one coordinate by `1`, so it changes the parity of exactly one coordinate.

Therefore:

* If both `x` and `y` are **even**, we can reach the destination using only long steps.
* If exactly one of `x` and `y` is **odd**, we can use one short step for that coordinate.
* If both `x` and `y` are **odd**, we would need two short steps, which is not allowed.

### Condition

```text
Number of odd coordinates <= 1
```

So:

```python
if x % 2 + y % 2 <= 1:
    print("YES")
else:
    print("NO")
```

---

## Python Solution

```python
import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        x, y = map(int, input().split())

        if x % 2 + y % 2 <= 1:
            print("YES")
        else:
            print("NO")


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
6
1 1
1 2
4 6
5 9
7 2
10 10
```

### Output

```text
NO
YES
YES
NO
YES
YES
```

---

## Key Takeaway

The problem can be solved entirely using **parity (odd/even)**.

> A maximum of one coordinate can be odd because only one short step is available.
