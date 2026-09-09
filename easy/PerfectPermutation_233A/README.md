# A. Perfect Permutation

## Problem Description

You are given an integer `n`. Your task is to construct a **perfect permutation** of size `n`.

A permutation `p` is called perfect if, for every index `i`:

* `p[p[i]] = i`
* `p[i] != i`

If no perfect permutation exists, print `-1`.

## Key Idea

The condition:

```text
p[p[i]] = i
```

means that applying the permutation twice should return every element to its original position.

Also:

```text
p[i] != i
```

means no element can remain in its original position.

Therefore, the elements must be arranged in pairs and swapped:

```text
1 ↔ 2
3 ↔ 4
5 ↔ 6
...
```

For example, when `n = 4`:

```text
1 2 3 4
↓ ↓ ↓ ↓
2 1 4 3
```

The permutation becomes:

```text
2 1 4 3
```

## Approach

* If `n` is odd, it is impossible to pair all elements.
* Print `-1`.
* If `n` is even, swap every pair of consecutive elements.

For example:

```text
n = 6

1 2 3 4 5 6
↓ ↓ ↓ ↓ ↓ ↓
2 1 4 3 6 5
```

## Algorithm

1. Read the value of `n`.
2. If `n` is odd, print `-1`.
3. Otherwise, iterate from `1` to `n` with a step of `2`.
4. For every pair `(i, i + 1)`, print `(i + 1, i)`.

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(n)`

## Python Solution

```python
n = int(input())

if n % 2 == 1:
    print(-1)
else:
    result = []

    for i in range(1, n + 1, 2):
        result.append(i + 1)
        result.append(i)

    print(*result)
```

## Example

### Input

```text
4
```

### Output

```text
2 1 4 3
```

### Explanation

For the permutation:

```text
p = [2, 1, 4, 3]
```

* `p[p[1]] = p[2] = 1`
* `p[p[2]] = p[1] = 2`
* `p[p[3]] = p[4] = 3`
* `p[p[4]] = p[3] = 4`

Also, no element remains in its original position.

Therefore, it is a **perfect permutation**.

---

**Platform:** Codeforces
**Problem:** A. Perfect Permutation
**Difficulty:** Easy
