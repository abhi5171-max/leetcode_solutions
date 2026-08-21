# B. Lucky Substring — Codeforces

## Problem Summary

Given a string `s` containing only digits, find the **lucky substring** that occurs the **maximum number of times**.

A lucky number/string:

* Contains only `4` and `7`
* Is non-empty
* Has no leading zeroes

If multiple lucky substrings occur the same maximum number of times, output the **lexicographically smallest** one.

If no lucky substring exists, print `-1`.

## Key Idea

Since `s` contains only digits, any valid lucky substring can contain only `4` and `7`.

The length of `s` is at most `50`, so we can simply:

1. Generate/check every substring of `s`.
2. Keep only substrings consisting entirely of `4` and `7`.
3. Count how many times each such substring occurs.
4. Find the substring with the highest frequency.
5. If frequencies are equal, choose the lexicographically smallest substring.

An important detail is that **substring occurrences can overlap**.

For example, in:

```text
444
```

the substring `"4"` occurs 3 times.

## Python 3 Solution

```python id="q7x2kd"
s = input().strip()

freq = {}

n = len(s)

for i in range(n):
    for j in range(i + 1, n + 1):
        sub = s[i:j]

        # A lucky substring contains only 4 and 7
        if all(c in "47" for c in sub):
            freq[sub] = freq.get(sub, 0) + 1

if not freq:
    print(-1)
else:
    # Maximum frequency first,
    # lexicographically smallest in case of a tie
    answer = min(freq, key=lambda x: (-freq[x], x))
    print(answer)
```

## Example 1

Input:

```text id="4h1d4f"
047
```

Lucky substrings include:

```text
4
7
47
```

Each occurs once.

The lexicographically smallest is:

```text
4
```

Output:

```text id="f9n4sx"
4
```

## Example 2

Input:

```text id="m7x8qp"
16
```

There are no `4` or `7` digits, so no lucky substring exists.

Output:

```text id="n2r8bc"
-1
```

## Example 3

Input:

```text id="w3k6pa"
472747
```

The substring `"7"` occurs three times, while the other lucky substrings occur fewer times.

Therefore:

```text id="v5j2lm"
7
```

## Complexity

There are `O(n²)` substrings, and checking whether each substring contains only `4` and `7` can take `O(n)`.

* **Time:** `O(n³)`
* **Space:** `O(n²)`

With `n ≤ 50`, this is easily fast enough.

## Concepts Used

* String traversal
* Substrings
* Frequency counting using a dictionary
* Lexicographical comparison
* Nested loops
* Python `min()` with a custom key
