# B. Ashmal — Codeforces Solution

## Problem Description

You are given an array of `n` strings. Starting with an empty string `s`, each string must be added either to the beginning or to the end of `s`.

The objective is to obtain the lexicographically smallest possible final string.

## Approach: Greedy Algorithm

Process the strings in their given order. For each string `x`, compare the two possible results:

- `x + s`: Add `x` to the beginning.
- `s + x`: Add `x` to the end.

If `x + s` is lexicographically smaller, update `s = x + s`. Otherwise, update `s = s + x`.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = input().split()

    s = ""

    for x in a:
        if x + s < s + x:
            s = x + s
        else:
            s = s + x

    print(s)
```

## Example

**Input

```text
3
4
amir rima amin nima
1
codeforces
3
a ab abc
```

**Output

```text
aminamirrimanima
codeforces
aababc
```

## Complexity Analysis

- **Time Complexity:** `O(L²)` in the worst case, where `L` is the total length of all strings in a test case.
- **Space Complexity:** `O(L)` for storing the resulting string.

## Key Concepts

- Greedy Algorithm
- String Concatenation
- Lexicographical Comparison
