# A. DBMB and the Array

## Problem

Given an array of `n` integers, a target value `k`, and an integer `x`, we can perform the following operation any number of times:

* Choose any index `i`.
* Add `x` to `a[i]`.

Determine whether it is possible to make the sum of the array exactly equal to `k`.

## Approach

Let the initial sum of the array be:

```text
sum = a[0] + a[1] + ... + a[n-1]
```

Every operation increases the total sum by exactly `x`.

Therefore, after `m` operations:

```text
sum + m × x = k
```

Rearranging:

```text
m = (k - sum) / x
```

For a valid solution:

1. `sum` must not be greater than `k`.
2. `k - sum` must be divisible by `x`.

So the condition is:

```text
sum <= k && (k - sum) % x == 0
```

## Algorithm

1. Read `n`, `k`, and `x`.
2. Calculate the sum of all array elements.
3. If `sum > k`, print `NO`.
4. Otherwise, check whether `(k - sum) % x == 0`.
5. If divisible, print `YES`; otherwise, print `NO`.

## Python Implementation

```python
t = int(input())

for _ in range(t):
    n, k, x = map(int, input().split())
    a = map(int, input().split())

    total = sum(a)

    if total <= k and (k - total) % x == 0:
        print("YES")
    else:
        print("NO")
```

## Complexity

* **Time Complexity:** `O(n)` per test case
* **Space Complexity:** `O(1)` extra space

## Key Concept

The important observation is that the operation changes the **total sum by exactly `x`**, regardless of which element is selected.

Therefore, this is essentially a **divisibility problem**.

## Tags

`Math` `Arrays` `Implementation` `Number Theory`
