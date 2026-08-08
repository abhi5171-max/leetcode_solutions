# Codeforces — A. Haiku

## Problem

A traditional haiku consists of three phrases containing exactly:

```text
5 syllables
7 syllables
5 syllables
```

For this problem, the number of syllables in a phrase is simplified to the **number of vowels** in that phrase.

The vowels considered are:

```text
a, e, i, o, u
```

We need to determine whether the three given lines contain exactly `5`, `7`, and `5` vowels respectively.

## Approach

Read the three lines and count the vowels in each line.

The required number of vowels is:

```text
[5, 7, 5]
```

For every line:

1. Iterate through all characters.
2. Check whether the character is a vowel.
3. Increment the vowel count.
4. Compare the count with the required value.

If any line has an incorrect number of vowels, print `NO`.

Otherwise, print `YES`.

## Complexity

Let `L` be the total number of characters in the three lines.

* **Time:** `O(L)`
* **Space:** `O(1)`

## Python 3

```python
vowels = set("aeiou")
required = [5, 7, 5]

for i in range(3):
    line = input()
    count = sum(1 for ch in line if ch in vowels)

    if count != required[i]:
        print("NO")
        break
else:
    print("YES")
```

## Example

### Input

```text
on  codeforces 
beta round is running
   a rustling of keys 
```

### Output

```text
YES
```

The vowel counts are:

```text
First phrase  → 5
Second phrase → 7
Third phrase  → 5
```

Therefore, it is a valid haiku.

## Key Concept

**String processing / Character counting**
