# 125. Valid Palindrome

## Problem Statement

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward.

Alphanumeric characters include letters and numbers.

Given a string `s`, return `true` if it is a palindrome, or `false` otherwise.

## Examples

### Example 1

**Input:**
```text
s = "A man, a plan, a canal: Panama"
```

**Output:**
```text
true
```

**Explanation:**
```text
"amanaplanacanalpanama" is a palindrome.
```

### Example 2

**Input:**
```text
s = "race a car"
```

**Output:**
```text
false
```

**Explanation:**
```text
"raceacar" is not a palindrome.
```

### Example 3

**Input:**
```text
s = " "
```

**Output:**
```text
true
```

**Explanation:**
After removing non-alphanumeric characters, the string becomes empty (`""`), which is considered a palindrome.

## Approach

### Two-Pointer Technique

1. Initialize two pointers:
   - `left` at the beginning of the string.
   - `right` at the end of the string.
2. Skip all non-alphanumeric characters using `isalnum()`.
3. Compare characters after converting them to lowercase.
4. If any pair does not match, return `False`.
5. Continue until the pointers meet.
6. If all characters match, return `True`.

## Python Solution

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1

            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
```

## Complexity Analysis

- **Time Complexity:** O(n)
  - Each character is visited at most once.

- **Space Complexity:** O(1)
  - No extra space is used apart from a few variables.

## Tags

- String
- Two Pointers