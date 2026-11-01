# A. Equal Occurrences

**Platform:** Codeforces  
**Problem:** [A. Equal Occurrences](https://codeforces.com/problemset/problem/)

## Problem Description

Given a non-decreasing array of `n` integers, find the length of its longest balanced subsequence.

An array is called balanced if every distinct element appears the same number of times.

An empty array is also considered balanced.

## Approach: Frequency Counting + Greedy

1. Since the array is sorted, equal elements appear consecutively.
2. Count the frequency of each distinct element.
3. Sort the frequency array in ascending order.
4. Consider selecting the elements with the largest frequencies.
5. For each position `i`, calculate:

   `freq[i] * (k - i)`

   where `k` is the total number of distinct elements.

6. The maximum calculated value is the answer.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    freq = []

    i = 0
    while i < n:
        j = i

        while j < n and a[j] == a[i]:
            j += 1

        freq.append(j - i)
        i = j

    freq.sort()

    ans = 0
    k = len(freq)

    for i in range(k):
        ans = max(ans, freq[i] * (k - i))

    print(ans)
```

## Complexity Analysis

- **Time Complexity:** O(n log n)
- **Space Complexity:** O(n)

## Key Concepts

- Frequency Counting
- Greedy Algorithm
- Sorting
- Array Traversal
- Subsequences

## Key Takeaway

By selecting elements with the highest frequencies and reducing their occurrences to a common frequency, we can maximise the length of a balanced subsequence.

**Problem Status:** Solved
