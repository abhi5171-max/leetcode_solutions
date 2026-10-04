# Codeforces — A. Array Coloring

## Problem

You are given `n` distinct integers arranged in a row. Each card must be colored either **red** or **blue**.

The coloring must satisfy two conditions:

1. Adjacent cards in the original array must have different colors.
2. After sorting the cards in increasing order, adjacent cards must also have different colors.

Determine whether such a coloring is possible.

## Approach

Since adjacent cards in the original array must have different colors, we can assign colors according to their **position parity**:

- Even position → one color
- Odd position → the other color

This automatically satisfies the first condition.

Now consider the sorted array:

```text
1, 2, 3, ..., n
```

For every pair of consecutive values `x` and `x + 1`, their cards must have different colors.

Therefore, their original positions must have different parity:

```text
pos[x] % 2 != pos[x + 1] % 2
```

If any consecutive values have positions with the same parity, they would receive the same color, making the required coloring impossible.

## Algorithm

For each test case:

1. Read the array.
2. Create a `pos` array where `pos[x]` stores the original position of value `x`.
3. For every `x` from `1` to `n - 1`:
   - Check whether `pos[x]` and `pos[x + 1]` have different parity.
4. If all pairs satisfy the condition, print `YES`.
5. Otherwise, print `NO`.

## Example

### Input

```text
4
4
2 3 4 1
3
2 3 1
5
3 4 1 2 5
5
3 1 4 2 5
```

### Output

```text
YES
NO
YES
NO
```

## Complexity

For each test case:

- **Time Complexity:** `O(n)`
- **Space Complexity:** `O(n)`

## Key Observation

The problem can be reduced to checking the parity of the original positions of consecutive values:

```text
pos[x] % 2 != pos[x + 1] % 2
```

If this holds for every `x`, the answer is `YES`; otherwise, it is `NO`.
