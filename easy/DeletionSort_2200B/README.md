# README

## Codeforces – B. Deletion Sort

## Problem

You are given an array of positive integers. While the array is **not non-decreasing**, you may remove any one element.

Your task is to determine the **minimum possible number of elements remaining** when the array becomes non-decreasing.

### Key Observation

A single element is always a non-decreasing array.

Therefore:

* If the array is already non-decreasing, **no element can be removed**, so the answer is `n`.
* Otherwise, we can keep removing elements until only **one element** remains, which is always sorted.

So the answer is simply:

```text
n, if the array is already sorted
1, otherwise
```

### Complexity

For each test case:

* **Time:** `O(n)`
* **Space:** `O(n)` for storing the array.

Since `n ≤ 10`, this is easily within the limits.

---

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    if all(a[i] <= a[i + 1] for i in range(n - 1)):
        print(n)
    else:
        print(1)
```

### Example

Input

```text
3
4
1 4 2 3
1
100
2
6 7
```

Output

```text
1
1
2
```

### Explanation

* `[1, 4, 2, 3]` is not sorted → remove elements until one remains → `1`
* `[100]` is already sorted → cannot remove anything → `1`
* `[6, 7]` is already non-decreasing → cannot remove anything → `2`
