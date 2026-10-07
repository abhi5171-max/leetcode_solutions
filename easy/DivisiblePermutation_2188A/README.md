# A. Divisible Permutation

## Problem

Given an integer `n`, construct a permutation `p` of length `n` such that:

\[
|p_i-p_{i+1}|
\]

is divisible by `i` for every:

\[
1 \leq i \leq n-1
\]

A permutation contains every integer from `1` to `n` exactly once.

---

## Example

### Input

```text
2
2
3
```

### Output

```text
1 2
2 3 1
```

Multiple valid permutations may exist.

---

## Approach

The important observation is to construct the permutation **from the end**.

For the last two elements, we need:

\[
|p_{n-1}-p_n|
\]

to be divisible by `n-1`.

Since all values are between `1` and `n` and are distinct, the only possible difference is:

\[
n-1
\]

Therefore, we can start with:

```text
[1, n]
```

We then work backwards.

For a current position with required difference `i`, if the previous value is `x`, the next value must be either:

```text
x - i
```

or

```text
x + i
```

We select the valid unused value.

Finally, we reverse the constructed array because we built it from right to left.

---

## Algorithm

1. Start with:

   p = [1, n]

2. Maintain a set `used` containing the values already selected.
3. Iterate `i` from `n - 2` down to `1`.
4. Let `prev = p[-1]`.
5. Try `prev - i`.
6. If it is within `[1, n]` and unused, add it.
7. Otherwise, use `prev + i`.
8. Reverse the array.
9. Print the resulting permutation.

---

## Python Solution

```python
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input())

    p = [1, n]
    used = {1, n}

    for i in range(n - 2, 0, -1):
        prev = p[-1]

        if 1 <= prev - i <= n and prev - i not in used:
            p.append(prev - i)
            used.add(prev - i)
        else:
            p.append(prev + i)
            used.add(prev + i)

    p.reverse()
    print(*p)
```

---

## Example Walkthrough

Consider:

```text
n = 5
```

Start:

```text
[1, 5]
```

### Step 1

`i = 3`

```text
5 - 3 = 2
```

So:

```text
[1, 5, 2]
```

### Step 2

`i = 2`

```text
2 - 2 = 0
```

Invalid, so:

```text
2 + 2 = 4
```

Now:

```text
[1, 5, 2, 4]
```

### Step 3

`i = 1`

```text
4 - 1 = 3
```

Now:

```text
[1, 5, 2, 4, 3]
```

Reverse it:

```text
3 4 2 5 1
```

### Verification

```text
|3 - 4| = 1  → divisible by 1 ✓
|4 - 2| = 2  → divisible by 2 ✓
|2 - 5| = 3  → divisible by 3 ✓
|5 - 1| = 4  → divisible by 4 ✓
```

Therefore:

```text
3 4 2 5 1
```

is a valid permutation.

---

## Complexity

For each test case:

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

With:

```text
1 ≤ t ≤ 100
2 ≤ n ≤ 100
```

the solution easily satisfies the time and memory limits.

---

## Key Takeaway

The main trick is:

> **Build the permutation backwards, starting with `[1, n]`, and make consecutive elements differ by the required index.**

This avoids brute force and guarantees a valid permutation.

---
