# Make `a` Divisible by `b`

## Problem Statement

Given two positive integers `a` and `b`, determine the minimum number of increments needed to make `a` divisible by `b`. In one move, you may increase `a` by **1**.

---

## Approach

To make `a` divisible by `b`, we first calculate the remainder:

```text
remainder = a % b
```

* If the remainder is `0`, `a` is already divisible by `b`, so the answer is `0`.
* Otherwise, the minimum increments required are:

```text
b - remainder
```

A compact formula that works for both cases is:

```text
(b - (a % b)) % b
```

The extra modulo ensures that when `a` is already divisible by `b`, the result is `0` instead of `b`.

---

## Algorithm

1. Read the number of test cases.
2. For each test case:

   * Read `a` and `b`.
   * Compute:

   ```text
   answer = (b - (a % b)) % b
   ```

   * Print the answer.

---

## Correctness

* If `a % b == 0`, no moves are needed.
* Otherwise, adding `b - (a % b)` makes `a` exactly equal to the next multiple of `b`.
* Since this is the smallest possible increase, the computed value is the minimum number of moves.

---

## Complexity Analysis

* **Time Complexity:** `O(t)`
* **Space Complexity:** `O(1)`

---

## Python Solution

```python
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    print((b - (a % b)) % b)
```

---

## Key Concepts

* Modulo Arithmetic
* Mathematical Observation
* Constant-Time Computation
