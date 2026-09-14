# A. Divide and Conquer

## Problem Statement

You are given two positive integers `x` and `y`.

You can perform the following operation any number of times:

1. Choose a positive integer `z` such that `z` divides `x`.
2. Set:

   `x = x / z`

Determine whether it is possible to make `x` exactly equal to `y`.

---

## Approach

In every operation, we divide `x` by one of its divisors. Therefore, the value of `x` can only become one of its divisors.

So, we can make `x` equal to `y` if and only if `y` divides `x`.

We simply check:

```text
x % y == 0
```

* If true, print `YES`.
* Otherwise, print `NO`.

---

## Complexity

* **Time Complexity:** `O(t)`
* **Space Complexity:** `O(1)`

---

## Example

### Input

```text
3
12 2
6 7
99 79
```

### Output

```text
YES
NO
NO
```
