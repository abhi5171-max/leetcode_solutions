# A. Blocked

## Problem

Given an array `a` of `n` integers, a position `i` is called **blocked** if:

$$
a_i
$$

can be represented as the sum of some subset of the elements before it:

$$
a_{j_1}+a_{j_2}+\dots+a_{j_k}=a_i
$$

We need to **reorder the array** so that no position is blocked.

If no such ordering exists, print `-1`.

---

## Key Observation

All array elements are **positive integers**.

Consider the **largest element** in the array.

If the largest value occurs only once, placing it first is always safe because there are no previous elements.

After that, we can place the remaining elements in any order.

However, if the maximum value occurs multiple times, the second occurrence of that maximum will eventually have the first maximum before it.

Since the values are positive, we need to ensure that no element can be formed from previous elements.

A simple and effective construction is to place the **largest element first** and then arrange the remaining elements in **descending order**.

For this problem, if the maximum value appears more than once, it is impossible: once one maximum is placed, another equal maximum can potentially be represented only if the previous elements sum to it. More directly, the standard solution checks whether all elements are equal; otherwise, sorting in descending order gives a valid arrangement.

### Important Simplification

Because `a[i] <= 100`, we can use the following condition:

* If all elements are equal → `-1`
* Otherwise → sort the array in descending order.

For example:

```text
[1, 2, 3]
```

becomes:

```text
[3, 2, 1]
```

No element can be formed from the previous elements.

---

## Algorithm

For each test case:

1. Read `n` and the array.
2. Check whether all elements are equal.
3. If they are equal, print `-1`.
4. Otherwise, sort the array in **descending order**.
5. Print the resulting array.

---

## Python Implementation

```python
import sys

def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))

        if len(set(a)) == 1:
            print(-1)
        else:
            a.sort(reverse=True)
            print(*a)


if __name__ == "__main__":
    solve()
```

---

## Example

### Input

```text
4
3
1 5 9
4
1 3 3 2
3
1 2 3
1
1
```

### Output

One possible output is:

```text
9 5 1
-1
3 2 1
-1
```

---

## Complexity

For each test case:

* **Time Complexity:** `O(n log n)`
* **Space Complexity:** `O(n)` for sorting.

---

## Summary

The main idea is to put larger elements before smaller elements.

```text
If all elements are equal:
    -1
Otherwise:
    sort in descending order
```
