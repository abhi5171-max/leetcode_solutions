# Codeforces - A. Dr. TC

## Problem

Given a binary string `s` of length `n`, create `n` binary strings. Each string is initially a copy of `s`, but its corresponding position is flipped:

- `0` becomes `1`.
- `1` becomes `0`.

The task is to calculate the total number of `1`s across all generated strings.

## Approach: Counting + Mathematical Observation

Let `ones` represent the number of `1`s in the original string.

There are:
- `ones` positions containing `1`.
- `n - ones` positions containing `0`.

When a `0` is flipped to `1`, that row contains `ones + 1` ones.

When a `1` is flipped to `0`, that row contains `ones - 1` ones.

Therefore, the total number of ones is:

```text
(n - ones) * (ones + 1) + ones * (ones - 1)
```

After simplification:

```text
answer = n + (n - 2) * ones
```

This formula avoids constructing all `n` binary strings.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    s = input()

    ones = s.count('1')

    ans = n + (n - 2) * ones

    print(ans)
```

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case, because counting the ones takes linear time.
- **Space Complexity:** `O(1)` auxiliary space.

## Key Concepts

- Binary Strings
- String Counting
- Mathematical Simplification
- Frequency Counting

## Key Takeaway

When a problem asks for the total result of many similar operations, look for a mathematical pattern. Counting the number of zeros and ones allows us to calculate the answer directly without generating every modified string.
