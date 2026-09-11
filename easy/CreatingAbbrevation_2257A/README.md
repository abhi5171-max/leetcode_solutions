# A. Creating Abbreviations

## Problem

The Beaver initially has a set `S` containing `n` ordinary words.

He can perform the following operation:

1. Choose a sequence of one or more words from `S`. The same word can be used multiple times.
2. Create an abbreviation using the first letter of each word in the sequence.
3. Add the newly created abbreviation to `S`, so it can be used as a word in future operations.

Given the initial words and a set of abbreviations, determine whether there exists an order in which all abbreviations could have been created.

---

## Key Observation

To create an abbreviation, every character in it must be the first letter of some word currently available.

For example:

```text
apple   → A
banana  → B
cherry  → C
```

Initially, we can create abbreviations using only:

```text
A, B, C
```

Now suppose we create a new abbreviation:

```text
ABC
```

The newly created word also starts with `A`.

However, `A` was already available because we needed a word starting with `A` to create `ABC`.

Therefore, **creating new abbreviations never introduces a new starting letter**.

So, we only need to check whether every character of every abbreviation is present among the first letters of the initial words.

---

## Algorithm

For each test case:

1. Create a set containing the uppercase first letter of every ordinary word.
2. For every abbreviation:

   * Check each character.
   * If any character is not in the set, print `NO`.
3. Otherwise, print `YES`.

---

## Complexity

Let `L` be the total length of all abbreviations.

* **Time Complexity:** `O(n + L)`
* **Space Complexity:** `O(26)` ≈ `O(1)`

---

## Python 3 Solution

```python
import sys


def solve():
    input = sys.stdin.readline

    t = int(input())

    for _ in range(t):
        n, m = map(int, input().split())

        # Store the first letters of all initial words
        available = set()

        for _ in range(n):
            word = input().strip()
            available.add(word[0].upper())

        possible = True

        # Check every abbreviation
        for _ in range(m):
            abbreviation = input().strip()

            for char in abbreviation:
                if char not in available:
                    possible = False

        print("YES" if possible else "NO")


if __name__ == "__main__":
    solve()
```

---

## Example

### Input

```text
4
6 4
apple
grand
banana
great
cherry
good
AG
BG
CG
ABC
1 1
apple
AA
1 2
apple
A
AA
2 2
apple
avocado
B
BA
```

### Output

```text
YES
YES
YES
NO
```

---

## Explanation

For the first test case, the available starting letters are:

```text
A, G, B, C
```

All characters in:

```text
AG
BG
CG
ABC
```
