# README — Codeforces A. Homework

## Problem Description

Given a string of lowercase Latin letters and an integer `k`, we can delete **at most `k` characters** from the string.

The goal is to minimize the number of **distinct characters remaining** in the string.

We must output:

1. The minimum possible number of distinct characters.
2. A valid resulting subsequence.

## Approach

The key observation is that if we want to completely remove a character, we must delete **all occurrences** of that character.

Therefore:

1. Count the frequency of every character.
2. Sort characters by their frequency in ascending order.
3. Starting from the least frequent character:

   * If its frequency is `<= k`, delete all its occurrences.
   * Subtract its frequency from `k`.
   * Otherwise, keep the character.
4. The remaining characters give the minimum possible number of distinct characters.

Why remove the least frequent characters first?

If we have limited deletions, removing a character with fewer occurrences costs less and eliminates one distinct character. This maximizes the number of distinct characters we can completely eliminate.

### Example

For:

```text
abacaba
k = 4
```

Frequencies:

```text
a → 4
b → 2
c → 1
```

Remove `c`:

```text
k = 4 - 1 = 3
```

Remove `b`:

```text
k = 3 - 2 = 1
```

We cannot remove `a` because it requires 4 deletions.

Remaining string:

```text
aaaa
```

So the answer is:

```text
1
aaaa
```

## Python 3 Solution

```python
from collections import Counter

s = input().strip()
k = int(input())

freq = Counter(s)

# Characters sorted by frequency
chars = sorted(freq, key=freq.get)

removed = set()

for ch in chars:
    if freq[ch] <= k:
        k -= freq[ch]
        removed.add(ch)
    else:
        break

# Build the resulting subsequence
result = ''.join(ch for ch in s if ch not in removed)

print(len(set(result)))
print(result)
```

## Complexity

Let `n` be the length of the string.

* Frequency counting: `O(n)`
* Sorting at most 26 lowercase letters: `O(26 log 26)`, effectively `O(1)`
* Constructing the result: `O(n)`

Therefore:

**Time Complexity:** `O(n)`

**Space Complexity:** `O(n)` for the resulting string and frequency storage.

## Key Idea

> **To minimize distinct characters, completely remove the least frequent characters first.**

This greedy strategy gives the optimal answer because every removed character eliminates exactly one distinct character, and choosing the smallest frequency minimizes the number of deletions required.
