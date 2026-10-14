# A. New Year String

## Problem Description

A string is called a **New Year string** if it contains `"2026"` as a continuous substring or does not contain `"2025"` as a continuous substring.

In one operation, we can replace any character with `0`, `2`, `5`, or `6`. Find the minimum number of operations required to make the string a New Year string.

## Approach

1. Read the number of test cases `t`.
2. For each test case, read the string `s`.
3. If `"2026"` is present in `s`, the string already satisfies the condition, so print `0`.
4. If `"2025"` is absent from `s`, the string also satisfies the condition, so print `0`.
5. Otherwise, print `1`, because changing the last character of an occurrence of `"2025"` to `6` creates `"2026"`.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    s = input().strip()

    if "2026" in s or "2025" not in s:
        print(0)
    else:
        print(1)
```

## Example

**Input

```text
7
4
0000
4
2025
4
2026
8
20252026
8
20252025
9
202520256
9
202520265
```

**Output

```text
0
1
0
0
1
1
0
```

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case, where `n` is the length of the string.
- **Auxiliary Space Complexity:** `O(1)`, excluding the input string.

## Key Takeaway

A single character replacement is sufficient whenever the string contains `"2025"` but does not contain `"2026"`. Otherwise, no operations are required.
