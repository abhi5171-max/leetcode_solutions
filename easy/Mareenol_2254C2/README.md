# Codeforces C2. Marenol (Hard Version)

## Problem Description

Given two binary strings `a` and `b` of length `n`, transform `a` into `b` using the minimum number of operations.

Allowed operations:

- `001 ↔ 100`
- `110 ↔ 011`

If transformation is impossible, print `-1`.

## Approach

Each operation swaps characters at positions `i` and `i + 2`. Therefore, odd-indexed positions and even-indexed positions form two independent groups.

For each group:

1. Collect the positions of all `1`s in `a` and `b`.
2. If the counts differ, the transformation is impossible.
3. Otherwise, match the positions of the `1`s in their original order.
4. Each matched pair contributes `abs(x - y) // 2` operations.

The minimum number of operations is the sum of these distances across both groups.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = input().strip()
    b = input().strip()

    ans = 0
    possible = True

    for parity in range(2):
        pos_a = [i for i in range(parity, n, 2) if a[i] == '1']
        pos_b = [i for i in range(parity, n, 2) if b[i] == '1']

        if len(pos_a) != len(pos_b):
            possible = False
            break

        for x, y in zip(pos_a, pos_b):
            ans += abs(x - y) // 2

    print(ans if possible else -1)
```

## Example

**Input

```text
5
4
0100
0001
4
0100
0010
6
110000
000011
8
10101010
10101010
5
01001
10010
```

**Output

```text
1
-1
4
0
3
```

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case.
- **Space Complexity:** `O(n)` for storing the positions of `1`s.

The sum of `n` across all test cases is at most `2 × 10^5`, so this solution is efficient enough.

## Topics

- Greedy
- Strings
- Binary Strings
- Two Pointers
- Position Matching
