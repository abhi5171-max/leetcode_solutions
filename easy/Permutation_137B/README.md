# B. Permutation

## Problem Statement

You are given a sequence of `n` integers.

A sequence is called a **permutation** if it contains every integer from `1` to `n` exactly once.

You may change any element into another integer. Find the **minimum number of changes** required to transform the given sequence into a permutation.

You cannot add or remove elements.

---

## Approach

A valid permutation of size `n` must contain:

```text
1, 2, 3, ..., n
```

exactly once.

Therefore:

1. Count how many times each number from `1` to `n` appears.
2. If a number appears more than once, only one occurrence can remain.
3. Every extra occurrence must be changed into a missing number.
4. Hence, the answer is the total number of duplicate occurrences.

For example:

```text
5 3 3 3 1
```

For `n = 5`, the required numbers are:

```text
1 2 3 4 5
```

The number `3` appears three times, so two of those occurrences are duplicates.

Missing numbers are `2` and `4`, so we need:

```text
3 → 4
3 → 2
```

Therefore, the answer is `2`.

---

## Algorithm

* Create a frequency array of size `n + 1`.
* Traverse all elements.
* For every `a[i]`:

  * If it is within `1...n` and has already appeared, increment the answer.
  * Otherwise, mark it as seen.
* Print the answer.

Since the input guarantees `a[i] <= 5000`, an array can be used safely.

---

## Python 3 Solution

```python
n = int(input())
a = list(map(int, input().split()))

seen = [False] * (n + 1)
changes = 0

for x in a:
    if 1 <= x <= n:
        if seen[x]:
            changes += 1
        else:
            seen[x] = True
    else:
        changes += 1

print(changes)
```

---

## Example 1

### Input

```text
3
3 1 2
```

### Analysis

All numbers from `1` to `3` appear exactly once:

```text
1 2 3
```

No changes are required.

### Output

```text
0
```

---

## Example 2

### Input

```text
2
2 2
```

Number `2` appears twice, while `1` is missing.

Change one `2` into `1`.

### Output

```text
1
```

---

## Example 3

### Input

```text
5
5 3 3 3 1
```

Required:

```text
1 2 3 4 5
```

Present:

```text
1, 3, 5
```

Missing:

```text
2, 4
```

There are two extra occurrences of `3`, so two changes are required.

### Output

```text
2
```

---

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

---

## Key Takeaway

The minimum number of changes is exactly the number of **duplicate or invalid elements**, because every such element can be replaced by one of the missing values to form a valid permutation.
