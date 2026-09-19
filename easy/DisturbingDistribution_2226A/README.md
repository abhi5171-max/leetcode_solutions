# Codeforces A. Disturbing Distribution

## Problem

Given an array `a`, we can repeatedly choose a **non-decreasing subsequence** and remove it.

The cost of removing a subsequence is the **product of all its elements**.

The goal is to remove the entire array with the **minimum possible total cost**.

Since the answer can be very large, it must be reported modulo:

```text
676767677
```

---

## Key Observation

The important part is the difference between `1` and numbers greater than `1`.

For any two numbers `x, y > 1`:

```text
x × y >= x + y
```

For example:

```text
2 × 3 = 6
2 + 3 = 5
```

Therefore, combining two elements greater than `1` into the same operation can never reduce the cost.

So every element `> 1` can simply be removed individually.

### What about `1`?

For any `x`:

```text
1 × x = x
```

Therefore, adding a `1` before a larger element does not increase the product.

This means the `1`s can be used together with later elements without increasing their cost.

The only `1`s that may require an additional cost are the `1`s **after the last element greater than `1`**, because there is no larger element after them to combine with.

---

## Algorithm

For every test case:

1. Add every element greater than `1` to the answer.
2. Find the position of the last element greater than `1`.
3. If there is at least one `1` after that position, add `1` to the answer.
4. If the entire array consists of `1`s, the answer is simply `1`.

---

## Example

Consider:

```text
1 2 1 2 3
```

The elements greater than `1` are:

```text
2 + 2 + 3 = 7
```

The last element greater than `1` is `3`, which is already at the end.

Therefore:

```text
Answer = 7
```

One possible grouping is:

```text
[1, 2, 2] → 1 × 2 × 2 = 4
[1, 3]    → 1 × 3 = 3

Total = 4 + 3 = 7
```

---

## Special Case

If the array contains only `1`s:

```text
1 1 1 1
```

We can remove all of them together:

```text
1 × 1 × 1 × 1 = 1
```

Therefore:

```text
Answer = 1
```

---

## Python Solution

```python
import sys

MOD = 676767677


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        ans = 0
        last_greater = -1

        for i, x in enumerate(a):
            if x > 1:
                ans += x
                last_greater = i

        # All elements are 1
        if last_greater == -1:
            print(1)
            continue

        # There is at least one 1 after the last element > 1
        if last_greater < n - 1:
            ans += 1

        print(ans % MOD)


if __name__ == "__main__":
    solve()
```

---

## Dry Run

### Input

```text
3
5
1 2 1 2 3
3
3 2 1
4
1 1 1 1
```

### Test Case 1

```text
1 2 1 2 3
```

Elements `> 1`:

```text
2 + 2 + 3 = 7
```

Last element `> 1` is `3`, and there is no element after it.

```text
Answer = 7
```

### Test Case 2

```text
3 2 1
```

Elements `> 1`:

```text
3 + 2 = 5
```

There is a `1` after the last element `> 1`.

```text
Answer = 5 + 1 = 6
```

### Test Case 3

```text
1 1 1 1
```

All elements are `1`.

```text
Answer = 1
```

### Output

```text
7
6
1
```

---

## Complexity

For each test case, we scan the array once.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)` for storing the array

The computation itself uses only `O(1)` extra space.

---

## Key Takeaway

The entire problem reduces to one simple greedy observation:

```text
Every element > 1 → pay it separately
1s before/among them → can be absorbed for free
1s after the last element > 1 → pay 1
All elements are 1 → pay 1
```

This gives a simple **greedy + mathematical** solution.
