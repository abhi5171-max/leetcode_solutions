# Help Vasilisa the Wise 2

## Problem Statement

We are given six required sums for a `2 × 2` square:

* `r1`, `r2` → sums of the two rows
* `c1`, `c2` → sums of the two columns
* `d1`, `d2` → sums of the two diagonals

We need to fill the square with **four distinct numbers from 1 to 9** such that all six required sums are satisfied.

If no valid arrangement exists, print `-1`.

---

## Approach

Let the square be:

```text
a b
c d
```

The required conditions are:

```text
a + b = r1
c + d = r2

a + c = c1
b + d = c2

a + d = d1
b + c = d2
```

Since there are only **9 possible digits**, we can use brute force.

Try every possible value for `a`, `b`, `c`, and `d` from `1` to `9`.

For each arrangement:

1. Make sure all four numbers are different.
2. Check the two row sums.
3. Check the two column sums.
4. Check both diagonal sums.
5. If every condition is satisfied, print the square.

There are only:

```text
9 × 8 × 7 × 6 = 3024
```

possible arrangements, so brute force is easily fast enough.

---

## Python 3 Solution

```python
r1, r2 = map(int, input().split())
c1, c2 = map(int, input().split())
d1, d2 = map(int, input().split())

for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):

                # All numbers must be different
                if len({a, b, c, d}) != 4:
                    continue

                # Check all required sums
                if a + b != r1:
                    continue
                if c + d != r2:
                    continue
                if a + c != c1:
                    continue
                if b + d != c2:
                    continue
                if a + d != d1:
                    continue
                if b + c != d2:
                    continue

                print(a, b)
                print(c, d)
                exit()

print(-1)
```

---

## Example

### Input

```text
3 7
4 6
5 5
```

Consider:

```text
1 2
3 4
```

Rows:

```text
1 + 2 = 3
3 + 4 = 7
```

Columns:

```text
1 + 3 = 4
2 + 4 = 6
```

Diagonals:

```text
1 + 4 = 5
2 + 3 = 5
```

All conditions are satisfied, so this is a valid answer.

### Output

```text
1 2
3 4
```

---

## Why Brute Force Works

There are only 9 digits available, and we need 4 distinct digits.

The maximum number of arrangements is:

```text
9P4 = 9 × 8 × 7 × 6 = 3024
```

Checking just 3024 possibilities is extremely small for the given time limit.

---

## Complexity

**Time Complexity:**

```text
O(9 × 8 × 7 × 6) = O(1)
```

Since the maximum number of combinations is fixed.

**Space Complexity:**

```text
O(1)
```

---

## Key Takeaway

For a very small search space, **brute force is often the simplest and safest solution**. Here, trying every arrangement of four distinct digits from `1` to `9` guarantees that we find a solution if one exists.
