# A. Chores

## Problem Statement

Petya and Vasya have `n` chores, where each chore has a complexity `hi`.

Petya wants to take all chores with complexity **greater than `x`**, while Vasya takes all chores with complexity **less than or equal to `x`**.

Petya must do exactly `a` chores and Vasya must do exactly `b` chores, where:

[
a+b=n
]

We need to find the number of integer values of `x` for which this division is possible.

---

## Approach

First, sort the array of chore complexities.

Suppose the sorted array is:

```text
h[0] <= h[1] <= ... <= h[n-1]
```

Vasya needs exactly `b` chores with:

```text
hi <= x
```

Therefore:

* The `b`-th smallest element must be `<= x`.
* The next element, `(b+1)`-th smallest, must be `> x`.

Using 0-based indexing, this gives:

```text
h[b - 1] <= x < h[b]
```

The number of integer values of `x` is therefore:

```text
h[b] - h[b - 1]
```

If these two values are equal, there are no valid values of `x`, and the answer is `0`.

---

## Algorithm

1. Read `n`, `a`, and `b`.
2. Read the chore complexities.
3. Sort the array.
4. Calculate:

   ```text
   answer = h[b] - h[b - 1]
   ```
5. Print the answer.

---

## Python 3 Solution

```python
n, a, b = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

answer = h[b] - h[b - 1]

print(answer)
```

---

## Example

### Input

```text
5 2 3
6 2 3 100 1
```

### Sorted Array

```text
1 2 3 6 100
```

Vasya needs `b = 3` chores.

Therefore:

```text
h[b - 1] = 3
h[b] = 6
```

So valid values satisfy:

```text
3 <= x < 6
```

The possible values are:

```text
3, 4, 5
```

Hence:

```text
Answer = 3
```

### Output

```text
3
```

---

## Complexity

* **Time Complexity:** `O(n log n)` due to sorting.
* **Space Complexity:** `O(n)` for storing the array.

---

## Key Insight

After sorting, the only boundary that matters is between the `b`-th and `(b+1)`-th smallest chore complexities.

The answer is simply:

```text
h[b] - h[b - 1]
```

This works because every integer `x` between these two values gives exactly `b` chores to Vasya and exactly `a` chores to Petya.
