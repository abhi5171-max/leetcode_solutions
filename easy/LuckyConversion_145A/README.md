Here’s a clean **README.md** with the Python 3 solution:

# A. Lucky Conversion

## Problem Statement

Petya has two strings `a` and `b` of the same length. Both strings contain only the lucky digits `4` and `7`.

He can perform two types of operations on string `a`:

1. Replace any digit with its opposite:

   * `4 → 7`
   * `7 → 4`
2. Swap any two digits in `a`.

The goal is to make `a` equal to `b` using the **minimum number of operations**.

---

## Approach

For every position where `a[i] != b[i]`, there are only two possible mismatch types:

* `4 → 7`
* `7 → 4`

Let:

* `cnt47` = number of `4 → 7` mismatches
* `cnt74` = number of `7 → 4` mismatches

A swap between one `4 → 7` mismatch and one `7 → 4` mismatch fixes **both mismatches in one operation**.

So, we can fix:

```text
min(cnt47, cnt74)
```

mismatches using swaps.

After that, the remaining mismatches are all of the same type, and each requires one replacement operation.

Therefore:

```text
answer = min(cnt47, cnt74) + abs(cnt47 - cnt74)
```

which simplifies to:

```text
answer = max(cnt47, cnt74)
```

---

## Python 3 Solution

```python
a = input().strip()
b = input().strip()

cnt47 = 0
cnt74 = 0

for x, y in zip(a, b):
    if x == '4' and y == '7':
        cnt47 += 1
    elif x == '7' and y == '4':
        cnt74 += 1

print(max(cnt47, cnt74))
```

---

## Example

### Input

```text
47
74
```

### Mismatches

```text
4 → 7
7 → 4
```

One swap fixes both positions.

### Output

```text
1
```

---

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

where `n` is the length of the strings.

---

## Key Insight

> Pair opposite mismatches using swaps first. Any remaining mismatches can be fixed individually by replacing the digit.

Thus, the minimum number of operations is simply:

```text
max(number of 4→7 mismatches, number of 7→4 mismatches)
```
