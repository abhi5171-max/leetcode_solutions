# Codeforces - A. Deranged Deletions

## Problem Statement

You are given an array `a` of length `n`.

You can delete any number of elements while preserving the order of the remaining elements.

Your task is to determine whether it is possible to obtain a non-empty array that is a derangement.

An array is called a derangement if, after sorting it in non-decreasing order, every element differs from the element at the same position in the original array.

If possible, print `YES` and any valid remaining array. Otherwise, print `NO`.

## Approach: Greedy + Adjacent Comparison

The key observation is that we only need two elements to construct a valid derangement.

### Case 1: A descending adjacent pair exists

If there is an index `i` such that:

`a[i] > a[i + 1]`

We can select these two elements.

For example:

Original pair: `[5, 2]`

After sorting: `[2, 5]`

Both positions contain different elements, so `[5, 2]` is a valid derangement.

Therefore, print `YES` and the pair.

### Case 2: No descending adjacent pair exists

If no adjacent pair satisfies `a[i] > a[i + 1]`, the original array is non-decreasing.

Every subsequence of a non-decreasing array is also non-decreasing.

After sorting, the array remains unchanged, so it cannot be a derangement.

Therefore, print `NO`.

## Python 3 Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    found = False

    for i in range(n - 1):
        if a[i] > a[i + 1]:
            print("YES")
            print(2)
            print(a[i], a[i + 1])
            found = True
            break

    if not found:
        print("NO")
```

## Example

**Input:**

```text
3
3
2 2 3
5
4 5 5 2 4
1
1
```

**Output:**

```text
NO
YES
2
5 2
NO
```

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case, because we traverse the array once.
- **Space Complexity:** `O(n)` for storing the input array.

## Key Learnings

- Identifying a valid subsequence using a greedy approach.
- Understanding derangements and sorted arrays.
- Using adjacent comparisons to detect descending pairs.
- Recognizing that a non-decreasing array cannot contain a deranged subsequence.

---

**Final Observation:**

If any adjacent pair satisfies `a[i] > a[i+1]`, the answer is `YES`. Otherwise, the answer is `NO`.