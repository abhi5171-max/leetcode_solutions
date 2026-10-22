# Length of Last Word

## Problem

Given a string `s` consisting of words and spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.

## Examples

**Example 1

Input:

```text
s = "Hello World"

Output:
```text
5
```

**Example

Input:

```text
s = "   fly me   to   the moon  "

Output:
```text
4
```

**Example 3

Input:

```text
s = "luffy is still joyboy"

Output:
```text
6
```

## Approach

1. Use Python's `split()` method to separate the words and ignore extra spaces.
2. Access the last word using `words[-1]`.
3. Return its length using `len()`.

## Python Solution

```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        return len(words[-1])
```

## Complexity Analysis

- **Time Complexity:** `O(n)` — the string is processed to identify its words.
- **Space Complexity:** `O(n)` — `split()` creates a list of words.

## Key Concepts

- String manipulation
- Python string methods
- List indexing
- Time and space complexity

## Platform

[LeetCode – Length of Last Word](https://leetcode.com/problems/length-of-last-word/)

**Language:** Python 3
