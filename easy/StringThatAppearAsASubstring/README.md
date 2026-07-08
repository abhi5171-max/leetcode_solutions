# Number of Strings That Appear as Substrings in Word

## Problem Statement

Given an array of strings `patterns` and a string `word`, determine how many strings in `patterns` appear as a substring of `word`.

## Approach

* Iterate through each string in `patterns`.
* Check whether it exists as a substring in `word` using Python's `in` operator.
* Count every successful match.

## Algorithm

1. Initialize a counter to `0`.
2. For each pattern in `patterns`:

   * If `pattern in word`, increment the counter.
3. Return the final count.

## Complexity Analysis

* **Time Complexity:** `O(n × m × k)` in the worst case, where:

  * `n` = number of patterns
  * `m` = length of `word`
  * `k` = average pattern length
* **Space Complexity:** `O(1)`

## Key Concepts

* Strings
* Substring Search
* Iteration
* Built-in String Operations

## Solution

```python
from typing import List

class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for pattern in patterns:
            if pattern in word:
                count += 1
        return count
```
