# Codeforces - A. Square Year

## Problem Statement

Given a year represented as a string of exactly four digits, determine whether it can be expressed in the form:

\[
(a+b)^2 = year
\]

where `a` and `b` are non-negative integers.

If such a pair exists, print any valid pair. Otherwise, print `-1`.

Leading zeros are allowed in the year representation.

## Approach: Perfect Square Check

The key observation is that the year must be a perfect square.

1. Convert the input string into an integer.
2. Calculate its integer square root using Python's `isqrt()`.
3. Check whether the square of the root equals the original number.
4. If it is a perfect square, print `0` and the square root.
5. Otherwise, print `-1`.

Choosing `a = 0` and `b = sqrt(year)` satisfies the required equation whenever the year is a perfect square.

## Python 3 Solution

```python
from math import isqrt

t = int(input())

for _ in range(t):
    s = input().strip()
    n = int(s)

    root = isqrt(n)

    if root * root == n:
        print(0, root)
    else:
        print(-1)
```

## Example

**Input:**
```text
5
0001
1001
1000
4900
2025
```

**Output:**
```text
0 1
-1
-1
0 70
0 45
```

## Complexity Analysis

- **Time Complexity:** O(1) per test case because the input always contains exactly four digits.
- **Space Complexity:** O(1) auxiliary space.

## Key Learning

- Checking whether a number is a perfect square.
- Using Python's `math.isqrt()` for accurate integer square-root calculation.
- Handling leading zeros when converting strings into integers.

---

**Language:** Python 3  
**Problem:** A. Square Year  
**Platform:** Codeforces
