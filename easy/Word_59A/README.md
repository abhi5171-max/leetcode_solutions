# Word - Codeforces

## Problem Statement

Given a word consisting of uppercase and lowercase Latin letters, convert the entire word to either uppercase or lowercase such that the minimum number of letters need to be changed.

* If the word contains strictly more uppercase letters, convert the whole word to uppercase.
* Otherwise (including when the counts are equal), convert the whole word to lowercase.

## Approach

1. Count the number of uppercase and lowercase letters.
2. Compare the counts:

   * If uppercase letters are more, convert the word to uppercase.
   * Otherwise, convert it to lowercase.

Python's built-in methods `.upper()` and `.lower()` are used for the conversion.

## Python Solution

```python
s = input()

upper = 0
lower = 0

for ch in s:
    if ch.isupper():
        upper += 1
    else:
        lower += 1

if upper > lower:
    print(s.upper())
else:
    print(s.lower())
```

## Example

### Input

```
HoUse
```

### Output

```
house
```

### Input

```
ViP
```

### Output

```
VIP
```

### Input

```
maTRIx
```

### Output

```
matrix
```

## Complexity Analysis

* **Time Complexity:** O(n)
* **Space Complexity:** O(1)

## Tags

`Strings` `Implementation`
