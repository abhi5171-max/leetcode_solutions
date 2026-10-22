# Letter Combinations of a Phone Number

## Problem

Given a string containing digits from `2` to `9`, return all possible letter combinations that the number could represent using the letters assigned to each digit on a telephone keypad.

## Example 1

**Input:**

```text

digits = "23"

**Output:**

```text
["ad","ae","af","bd","be","bf","cd","ce","cf"]
```

## Example 2

**Input:**

```text
digits = "2"

**Output:**
```text
["a","b","c"]
```

## Approach

1. Create a dictionary mapping each digit to its corresponding letters.
2. Initialize the result with an empty string.
3. Iterate through each digit and generate new combinations by appending every mapped letter to the existing combinations.
4. Update the result after processing each digit.
5. Return the final list of combinations.

## Python Solution

```python
class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        result = ['']

        for digit in digits:
            temp = []
            for combination in result:
                for letter in mapping[digit]:
                    temp.append(combination + letter)
            result = temp

        return result
```

## Complexity Analysis

- **Time Complexity:** `O(n × 4^n)` — each digit maps to at most four letters.
- **Space Complexity:** `O(n × 4^n)` — to store all generated combinations.

## Key Concepts

- Strings
- Hash Maps / Dictionaries
- Iteration
- Combinatorial Generation

## Platform

[LeetCode](https://leetcode.com/problems/letter-combinations-of-a-phone-number/)

**Language:** Python 3
