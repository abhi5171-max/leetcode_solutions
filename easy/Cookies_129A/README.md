# A. Cookies — Codeforces

## Problem Summary

You are given `n` bags containing `a[i]` cookies. Olga wants to steal **exactly one bag** such that the total number of cookies left in the remaining bags is **even**.

The task is to count how many bags can be stolen.

## Key Idea

Let the total number of cookies be:

`total = a1 + a2 + ... + an`

After stealing bag `i`, the remaining cookies are:

`total - a[i]`

We need:

`total - a[i]` to be even.

### Case 1: `total` is even

For the result to remain even:

* `even - even = even` ✅
* `even - odd = odd` ❌

So, we can steal **any bag containing an even number of cookies**.

### Case 2: `total` is odd

For the result to become even:

* `odd - odd = even` ✅
* `odd - even = odd` ❌

So, we can steal **any bag containing an odd number of cookies**.

Therefore:

> If the total sum is even, count even elements. Otherwise, count odd elements.

## Python 3 Solution

```python
n = int(input())
a = list(map(int, input().split()))

total = sum(a)

if total % 2 == 0:
    answer = sum(1 for x in a if x % 2 == 0)
else:
    answer = sum(1 for x in a if x % 2 == 1)

print(answer)
```

## Example

For:

```text
10
1 2 2 3 4 4 4 2 2 2
```

The total is `28`, which is even.

Even-valued bags:

```text
2 2 4 4 4 2 2 2
```

There are **8** such bags.

Output:

```text
8
```

## Complexity

* **Time:** `O(n)`
* **Space:** `O(n)` for storing the array

Since `n ≤ 100`, this easily fits within the limits.

## Concepts Used

* Array traversal
* Sum calculation
* Parity (odd/even)
* Conditional counting
* Python `sum()` and generator expressions
