# A. k-String

## Problem Statement

A string is called a **k-string** if it can be represented as `k` concatenated copies of the same string.

For example:

```text
azaz = "az" + "az"
```

So, `azaz` is a `2-string`.

Given a string `s` and an integer `k`, we need to rearrange the characters of `s` so that the resulting string becomes a `k-string`.

If it is impossible, print `-1`.

---

## Approach

For a string to consist of `k` identical parts, every character must be distributed equally among those `k` parts.

Therefore:

> The frequency of every character must be divisible by `k`.

### Example

```text
k = 2
s = aazz
```

Character frequencies:

```text
a = 2
z = 2
```

Both frequencies are divisible by `2`.

For one copy of the string:

```text
a → 2 / 2 = 1
z → 2 / 2 = 1
```

So, the base string can be:

```text
az
```

Repeating it `k` times:

```text
az + az = azaz
```

---

## Algorithm

1. Read `k` and string `s`.
2. Count the frequency of each character.
3. Check whether every frequency is divisible by `k`.
4. If any frequency is not divisible by `k`, print `-1`.
5. Otherwise:

   * Add each character `frequency // k` times to the base string.
   * Repeat the base string `k` times.
6. Print the result.

---

## Complexity Analysis

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

Where `n` is the length of the string.

---

## Python 3 Solution

```python
from collections import Counter

k = int(input())
s = input().strip()

freq = Counter(s)
base = []

for ch in sorted(freq):
    if freq[ch] % k != 0:
        print(-1)
        break
    base.append(ch * (freq[ch] // k))
else:
    print(''.join(base) * k)
```

---

## Examples

### Input

```text
2
aazz
```

### Output

```text
azaz
```

### Explanation

The string can be divided into two identical parts:

```text
az + az
```

Therefore, `azaz` is a valid `2-string`.
