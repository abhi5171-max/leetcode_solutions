# A. Three Numbers on the Blackboard — README

## Problem

You are given three non-negative integers `a`, `b`, and `c`.

In one operation, choose any one number and replace it with the sum of the other two.

For example:

```text
(3, 5, 11)
→ replace 11 with 3 + 5
→ (3, 5, 8)
```

You can perform the operation any number of times.

The goal is to find the **minimum possible range**:

```text
max(a, b, c) - min(a, b, c)
```

---

## Key Observation

Sort the three numbers:

```text
a <= b <= c
```

There are only a few useful possibilities.

### Case 1: No operation

The range is:

```text
c - a
```

### Case 2: Replace the largest number

Replace `c` with `a + b`.

The new numbers are:

```text
a, b, a + b
```

Since `a` and `b` are non-negative:

```text
range = max(a+b, b) - a
```

which is:

```text
a + b - a = b
```

So we can always achieve a range of `b`.

### Case 3: There is a zero

If:

```text
a = 0
```

then replacing `c` with:

```text
a + b = b
```

gives:

```text
0, b, b
```

and the range becomes:

```text
b
```

But if `b = 0`, we get:

```text
0, 0, 0
```

so the answer is `0`.

Therefore, after sorting, the answer is simply:

```text
min(c - a, b)
```

---

## Examples

### Example 1

```text
5 5 5
```

Already equal:

```text
range = 5 - 5 = 0
```

Answer:

```text
0
```

### Example 2

```text
4 6 9
```

Sorted:

```text
4 6 9
```

Original range:

```text
9 - 4 = 5
```

Replacing `9` with `4 + 6 = 10` gives a worse range.

So:

```text
min(5, 6) = 5
```

Answer:

```text
5
```

### Example 3

```text
2 3 10
```

Original range:

```text
10 - 2 = 8
```

Replace `10` with:

```text
2 + 3 = 5
```

We get:

```text
2 3 5
```

Range:

```text
5 - 2 = 3
```

Answer:

```text
3
```

---

## Python 3 Solution

```python
t = int(input())

for _ in range(t):
    a, b, c = map(int, input().split())

    a, b, c = sorted([a, b, c])

    answer = min(c - a, b)

    print(answer)
```

## Complexity

For each test case, sorting 3 numbers takes constant time:

```text
Time:  O(1) per test case
Space: O(1)
```

For `t` test cases:

```text
Time: O(t)
Space: O(1)
```

## Final Formula

After sorting:

```text
a <= b <= c
```

the answer is:

```text
min(c - a, b)
```

This gives the minimum possible range efficiently.
