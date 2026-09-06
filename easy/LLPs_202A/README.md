# A. LLPS - Lexicographically Largest Palindromic Subsequence

## Problem Description

Given a string `s` consisting of lowercase English letters, find the **lexicographically largest palindromic subsequence**.

A subsequence is obtained by deleting zero or more characters without changing the order of the remaining characters.

---

## Approach

The key observation is that the lexicographically largest palindrome should start with the **largest character** present in the string.

If the largest character appears multiple times, we can include **all of its occurrences**.

For example:

```text
s = "radar"

Largest character = 'r'
Occurrences = 2

Answer = "rr"
```

A string containing only repeated copies of the same character is always a palindrome.

Therefore:

1. Find the maximum character in the string.
2. Print all occurrences of that character.

---

## Python 3 Solution

```python
s = input()

mx = max(s)

print(mx * s.count(mx))
```

---

## Example

### Input

```text
bowwowwow
```

### Processing

```text
Maximum character = 'w'
Number of occurrences = 5
```

### Output

```text
wwwww
```

---

## Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

---

## Key Takeaway

To obtain the lexicographically largest palindromic subsequence, simply find the largest character in the string and include all of its occurrences. Since all selected characters are identical, the resulting subsequence is automatically a palindrome.
