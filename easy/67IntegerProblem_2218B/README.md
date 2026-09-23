# Codeforces — B. The 67th 6-7 Integer Problem

## Problem

You are given exactly **7 integers**.

You must negate exactly **6 out of the 7 integers**, meaning multiply those 6 integers by `-1`.

Among all possible choices, find the **maximum possible sum**.

---

## Key Observation

Suppose we choose `a[i]` as the only integer that is **not negated**.

Then the resulting sum is:

```text
a[i] - (sum of all other elements)
```

Let the total sum of all 7 elements be:

```text
S = a1 + a2 + ... + a7
```

If `a[i]` is left unchanged:

```text
result = a[i] - (S - a[i])
       = 2 * a[i] - S
```

Since `S` is fixed, we maximize the result by choosing the **largest element**.

Therefore:

```text
answer = 2 * max(a) - sum(a)
```

---

## Example

Consider:

```text
6 9 4 20 6 7 67
```

Total sum:

```text
S = 119
```

Maximum element:

```text
max(a) = 67
```

Therefore:

```text
answer = 2 × 67 - 119
       = 134 - 119
       = 15
```

So the answer is:

```text
15
```

---

## Algorithm

For each test case:

1. Read the 7 integers.
2. Calculate their total sum.
3. Find the maximum element.
4. Calculate:

```text
2 * max_element - total_sum
```

5 Print the result.

---

## Python Implementation

```python
import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        a = list(map(int, input().split()))

        total = sum(a)
        maximum = max(a)

        answer = 2 * maximum - total

        print(answer)


if __name__ == "__main__":
    solve()
```

---

## Complexity

There are exactly 7 elements in every test case.

* **Time Complexity:** `O(7)` → `O(1)` per test case
* **Space Complexity:** `O(7)` → `O(1)`

---

## Conclusion

Instead of trying all 7 possibilities, we can directly observe that the integer left **unnegated** should be the largest element.

### Formula

```text
answer = 2 × max(a) − sum(a)
```

This gives the maximum possible sum in constant time.
