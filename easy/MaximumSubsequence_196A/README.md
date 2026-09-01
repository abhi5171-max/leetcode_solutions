# Codeforces — A. Lexicographically Maximum Subsequence

## Problem Description

You are given a non-empty string `s` consisting only of lowercase English letters.

Your task is to find the **lexicographically maximum subsequence** of `s`.

A subsequence is obtained by deleting zero or more characters from the original string while keeping the relative order of the remaining characters.

---

## Approach

The key observation is that the lexicographically maximum subsequence should contain every character that is **not smaller than any character to its right**.

We can find these characters efficiently by scanning the string from **right to left**.

### Algorithm

1. Start from the last character of the string.
2. Keep track of the largest character encountered so far.
3. For every character:

   * If it is greater than or equal to the current maximum character, add it to the answer.
   * Otherwise, skip it.
4. Since we scanned from right to left, reverse the collected characters before printing.

### Example

For:

```text
ababba
```

Scanning from right to left:

```text
a → keep
b → keep
b → keep
a → skip
b → keep
a → skip
```

The selected characters in reverse order are:

```text
bbba
```

Reversing them gives:

```text
bbba
```

Therefore, the lexicographically maximum subsequence is:

```text
bbba
```

---

## Python 3 Solution

```python
s = input().strip()

result = []
max_char = ''

for ch in reversed(s):
    if not max_char or ch >= max_char:
        result.append(ch)
        max_char = ch

print(''.join(reversed(result)))
```

---

## Correctness

Suppose a character `s[i]` has a larger character somewhere to its right.

If we include `s[i]` before that larger character, the subsequence would be lexicographically smaller than one starting with the larger character. Therefore, `s[i]` should not be selected.

On the other hand, if `s[i]` is greater than or equal to every character to its right, keeping it cannot make the result worse. Thus, we keep it.

By applying this rule from right to left, we select exactly the characters necessary to form the lexicographically maximum subsequence.

---

## Complexity Analysis

Let `n` be the length of the string.

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

The solution easily handles strings of length up to `10⁵`.

---

## Example 1

### Input

```text
ababba
```

### Output

```text
bbba
```

---

## Example 2

### Input

```text
abbcbccacbbcbaaba
```

### Output

```text
cccccbba
```

---

## Key Takeaway

When finding a lexicographically maximum subsequence, scanning **from right to left** and keeping characters that are at least as large as the maximum seen so far provides a simple and efficient `O(n)` solution.
