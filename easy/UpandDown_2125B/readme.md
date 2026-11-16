# Codeforces - B. Left and Down

## Problem Statement

A robot starts at position `(a, b)` on an infinite grid. The goal is to move it to `(0, 0)`.

For a fixed integer `k`, each operation allows choosing two integers `dx` and `dy` such that:

`0 <= dx, dy <= k`

The robot moves from `(x, y)` to `(x - dx, y - dy)`.

The cost is:
- `1` if the chosen pair `(dx, dy)` is used for the first time.
- `0` if the same pair has been used before.

Find the minimum total cost required to reach `(0, 0)`.

## Approach: GCD + Mathematics

The minimum possible answer is always either `1` or `2`.

### Case 1: Answer is 1

If we can use the same pair `(dx, dy)` repeatedly, then:

`a = m * dx`

`b = m * dy`

The largest possible common multiplier is:

`g = gcd(a, b)`

Therefore, the smallest possible movement pair is:

`dx = a // g`

`dy = b // g`

This pair is valid if both coordinates are at most `k`.

The condition becomes:

`gcd(a, b) >= ceil(max(a, b) / k)`

### Case 2: Answer is 2

If the condition fails, we can always use two different pairs:

- `(1, 0)` repeatedly to reduce the x-coordinate.
- `(0, 1)` repeatedly to reduce the y-coordinate.

Since `k >= 1`, both pairs are valid.

Thus, the minimum cost is 2.

## Python 3 Solution

```python
from math import gcd

t = int(input())

for _ in range(t):
    a, b, k = map(int, input().split())

    g = gcd(a, b)
    required = (max(a, b) + k - 1) // k

    if g >= required:
        print(1)
    else:
        print(2)
```

## Example

**Input:**
```text
4
3 5 15
2 3 1
12 18 8
9 7 5
```

**Output:**
```text
1
2
1
2
```

## Complexity Analysis

- **Time Complexity:** `O(log(min(a, b)))` per test case, because of the Euclidean GCD algorithm.
- **Space Complexity:** `O(1)` auxiliary space.

## Key Learnings

- Understanding the Euclidean algorithm for GCD.
- Using GCD to identify a common multiplier.
- Converting movement constraints into a mathematical condition.
- Using integer ceiling division:
  
  `(x + k - 1) // k`

- Recognizing when an optimization problem has only two possible answers.

---

**Final Observation:**

If the reduced pair `(a / gcd, b / gcd)` fits within the limit `k`, the answer is `1`; otherwise, the answer is `2`.