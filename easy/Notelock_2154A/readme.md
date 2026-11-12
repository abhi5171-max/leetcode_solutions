# A. Notelock

**Platform:** Codeforces  
**Language:** Python 3  
**Topics:** Greedy, Strings, Implementation

## Problem Summary

Teto is playing a rhythm game represented by a binary string `s` of length `n`.

We can protect certain positions containing `1`.

Teto processes the string from left to right. She can change an unprotected `1` into `0` if there is no `1` among the previous `k-1` positions.

Our task is to find the minimum number of positions that must be protected so that the string remains unchanged.

## Approach: Greedy

### Key Observation

A position containing `1` does not need protection if there is another `1` within the previous `k-1` positions.

This is because the previous `1` will remain unchanged, preventing Teto from removing the current `1`.

However, if there is no previous `1` within that range, the current `1` must be protected.

### Algorithm

1. Initialize `ans = 0`.
2. Initialize `last = -k` to represent that no previous `1` has been encountered.
3. Traverse the string from left to right.
4. Whenever we encounter `1`:
   - If `i - last >= k`, protect this position and increment `ans`.
   - Update `last = i`.
5. Print the minimum number of protected positions.

## Python 3 Solution

```python
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = input().strip()

    ans = 0
    last = -k

    for i in range(n):
        if s[i] == '1':
            if i - last >= k:
                ans += 1
                last = i
            else:
                last = i

    print(ans)
```

## Example Dry Run

**Input:**

```text
4
2 2
11
7 2
1010101
7 4
1001001
8 3
00000000
```

### Test Case 1

`n = 2, k = 2`

String: `11`

- First `1`: Must be protected.
- Second `1`: Previous `1` is only 1 position away, so it is safe.

Answer: `1`

### Test Case 2

`n = 7, k = 2`

String: `1010101`

Positions of `1`: 0, 2, 4, 6.

Every consecutive pair has a distance of 2, which is greater than or equal to `k`.

Therefore, every `1` must be protected.

Answer: `4`

### Test Case 3

`n = 7, k = 4`

String: `1001001`

Positions of `1`: 0, 3, 6.

- Protect position 0.
- Position 3 is safe because the distance is 3, which is less than 4.
- Position 6 is also safe because the distance is 3.

Answer: `1`

### Test Case 4

`n = 8, k = 3`

String: `00000000`

There are no `1`s to protect.

Answer: `0`

**Output:**

```text
1
4
1
0
```

## Complexity Analysis

| Complexity | Value | Explanation |
|---|---|---|
| Time | O(n) | One traversal of the string |
| Space | O(1) | Only constant extra variables |

## Key Learnings

- Greedy algorithms can solve problems involving minimum protection or selection.
- Always examine the dependency between consecutive elements.
- A previously preserved element can prevent future elements from being modified.
- Careful index-distance analysis helps simplify string problems.

**Conclusion:** By tracking the previous occurrence of `1`, we can calculate the minimum number of protected positions in a single traversal.