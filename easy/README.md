# Codeforces — B. Your Name

## Problem

Given two strings `s` and `t`, determine whether the characters of `s` can be rearranged to form `t`.

## Approach

1. Read the number of test cases.
2. For each test case, read the string length `n` and the two strings.
3. Sort both strings alphabetically.
4. If the sorted strings are equal, print `YES`; otherwise, print `NO`.

Sorting allows us to compare the character frequencies of both strings.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    s, t_name = input().split()

    if sorted(s) == sorted(t_name):
        print("YES")
    else:
        print("NO")
```

## Example

**Input

```text
5
7
humitsa mitsuha
4
orhi hori
6
aakima makima
6
nezuqo nezuko
6
misaka mikasa
```

**Output

```text
YES
YES
NO
NO
YES
```

## Complexity Analysis

- **Time Complexity:** \(O(n \log n)\) per test case, due to sorting both strings.
- **Space Complexity:** \(O(n)\) for the sorted strings.

## Key Learning

Two strings are anagrams if they contain exactly the same characters with identical frequencies, regardless of their order.

**Language:** Python 3
