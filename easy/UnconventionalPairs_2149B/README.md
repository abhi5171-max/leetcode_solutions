# B. Unconventional Pairs

**Platform:** Codeforces  
**Problem:** [B. Unconventional Pairs](https://codeforces.com/problemset/problem/1771/B)  
**Language:** Python 3  
**Topics:** Sorting, Greedy Algorithms, Arrays

## Problem Statement

Given an array of `n` integers, where `n` is even, divide the elements into exactly `n/2` pairs. The difference of a pair `(x, y)` is `|x - y|`.

The objective is to minimize the maximum difference among all pairs.

## Approach

1. Sort the array in ascending order.
2. Pair adjacent elements: `(a[0], a[1])`, `(a[2], a[3])`, and so on.
3. Calculate the difference of each pair.
4. Return the maximum difference among these pairs.

### Why Does This Work?

Sorting places similar values next to each other. Pairing adjacent elements minimizes the maximum difference because pairing distant elements would leave other elements with potentially larger differences.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    a.sort()

    ans = 0
    for i in range(0, n, 2):
        ans = max(ans, a[i + 1] - a[i])

    print(ans)
```

## Example

**Input

```text
5
2
1 2
4
10 1 2 9
6
3 8 9 3 3 2
8
5 5 5 5 5 5 5 5
4
-5 -1 2 6
```

**Output

```text
1
1
1
0
4
```

## Complexity Analysis

- **Time Complexity:** `O(n log n)` per test case, due to sorting.
- **Space Complexity:** `O(n)` for storing the array.

## Key Takeaway

Sorting and greedily pairing adjacent elements is an efficient way to minimize the maximum pair difference.
