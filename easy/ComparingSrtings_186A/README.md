# A. Comparing Strings

## Problem Description

Given two non-empty strings consisting of lowercase Latin letters, determine whether the second string can be obtained from the first string by **swapping exactly two characters**.

The strings are guaranteed to be different.

Print:

* `YES` if one swap can transform the first string into the second.
* `NO` otherwise.

---

## Approach

A single swap can change characters at **only two positions**.

Therefore:

1. The two strings must have the **same length**.
2. Find all positions where the strings are different.
3. There must be **exactly two** different positions.
4. The characters at those positions must be swapped.

For example:

```text
s = ab
t = ba
```

The strings differ at positions `0` and `1`.

```text
s[0] = a    t[1] = a
s[1] = b    t[0] = b
```

So swapping `a` and `b` transforms `ab` into `ba`.

Therefore, the answer is `YES`.

---

## Algorithm

1. Read the two strings `s` and `t`.
2. If their lengths are different, print `NO`.
3. Store the positions where `s[i] != t[i]`.
4. If there are not exactly two such positions, print `NO`.
5. Let these positions be `i` and `j`.
6. Check whether:

   ```text
   s[i] == t[j]
   s[j] == t[i]
   ```
7. If both conditions are true, print `YES`; otherwise print `NO`.

---

## Example 1

### Input

```text
ab
ba
```

### Output

```text
YES
```

### Explanation

Swap the two characters in `ab`:

```text
ab → ba
```

So the strings belong to the same race.

---

## Example 2

### Input

```text
aa
ab
```

### Output

```text
NO
```

### Explanation

The strings differ at only one position. A single swap cannot transform `aa` into `ab`.

---

## Implementation

```python
s = input()
t = input()

if len(s) != len(t):
    print("NO")
else:
    diff = []

    for i in range(len(s)):
        if s[i] != t[i]:
            diff.append(i)

    if len(diff) == 2:
        i, j = diff

        if s[i] == t[j] and s[j] == t[i]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
```

---

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

Only two differing positions are required, so the extra space remains constant.

---

## Key Takeaway

A single swap can change **at most two positions**.

Therefore, two different strings can be transformed into each other with one swap **if and only if**:

```text
They have the same length
        AND
They differ at exactly two positions
        AND
Those two characters are reversed
```
