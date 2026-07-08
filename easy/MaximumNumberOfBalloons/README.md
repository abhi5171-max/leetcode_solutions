# Maximum Number of Balloons

## Problem Statement

Given a string `text`, determine the maximum number of times the word **"balloon"** can be formed using the characters in `text`. Each character may be used only once.

## Approach

* Count the frequency of every character in `text`.
* The word **"balloon"** requires:

  * `b` → 1
  * `a` → 1
  * `l` → 2
  * `o` → 2
  * `n` → 1
* The answer is the minimum possible count among these required characters.

## Algorithm

1. Count the frequency of all characters using a hash map.
2. Compute:

   * `count['b']`
   * `count['a']`
   * `count['l'] // 2`
   * `count['o'] // 2`
   * `count['n']`
3. Return the minimum of these values.

## Complexity Analysis

* **Time Complexity:** `O(n)`, where `n` is the length of `text`.
* **Space Complexity:** `O(1)` (at most 26 lowercase English letters).

## Key Concepts

* Hash Map
* Frequency Counting
* Greedy Observation
* String Processing

## Solution

```python
from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = Counter(text)
        return min(
            count['b'],
            count['a'],
            count['l'] // 2,
            count['o'] // 2,
            count['n']
        )
```
