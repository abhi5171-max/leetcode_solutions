# Codeforces — A. String Rotation Game

## Problem

Given a string `s`, we can cyclically rotate it any number of times.

The **score** is the number of blocks in the resulting string.

A block is a maximal contiguous sequence of equal characters.

The goal is to find the maximum possible score after rotating the string.

## Approach

Consider the string as a **circle**.

A transition occurs whenever two neighboring characters are different:

```text
s[i] != s[(i + 1) % n]
```

Let the number of such transitions be `transitions`.

### Case 1: All circular neighbors are different

If every neighboring pair is different, then:

```text
transitions = n
```

No matter where we rotate, the number of blocks is `n`.

Example:

```text
abcd
```

Answer:

```text
4
```

### Case 2: At least one pair of neighboring characters is equal

If there is an equal neighboring pair, we can rotate the string so that this equal pair becomes the boundary between the last and first characters.

This prevents that pair from forming a block boundary in the final linear string.

Therefore, the maximum number of blocks becomes:

```text
transitions + 1
```

Example:

```text
abbc
```

Circular transitions:

```text
a → b  ✓
b → b  ✗
b → c  ✓
c → a  ✓
```

So:

```text
transitions = 3
answer = 3 + 1 = 4
```

## Algorithm

For each test case:

1. Traverse the circular string.
2. Count positions where adjacent characters are different.
3. Check whether at least one adjacent pair is equal.
4. If no equal pair exists, output `n`.
5. Otherwise, output `transitions + 1`.

## Complexity

For each test case:

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(1)`

## Example

### Input

```text
4
4
abcd
4
abbc
4
abba
6
abbccc
```

### Output

```text
4
4
3
4
```

## Key Observation

The important part is to treat the string as **circular** because rotation changes which pair of characters becomes the first/last boundary.

```text
Maximum Blocks =
    n                       if all circular neighbors differ
    transitions + 1         otherwise
```
