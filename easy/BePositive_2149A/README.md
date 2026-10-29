# A. Be Positive

**Platform:** Codeforces  
**Problem:** A. Be Positive  
**Language:** Python 3  
**Topics:** Greedy, Arrays, Implementation

## Problem Statement

Given an array containing only `-1`, `0`, and `1`, find the minimum number of operations required to make the product of all array elements strictly positive.

In one operation, choose an element and increase it by `1`.

## Approach

1. **Handle zeros:** Each `0` must become `1`, requiring one operation per zero.
2. **Count negative elements:** Each `-1` contributes a negative sign to the product.
3. **Check parity:** If the number of `-1` elements is odd, the product is negative after all zeros become positive. We must convert one `-1` into `1`, which requires two operations: `-1 → 0 → 1`.
4. Add these operations to obtain the minimum answer.

## Python Solution

```python
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    operations = 0
    negative_count = 0

    for x in a:
        if x == 0:
            operations += 1
        elif x == -1:
            negative_count += 1

    if negative_count % 2 == 1:
        operations += 2

    print(operations)
```

## Example

**Input

```text
3
3
-1 0 1
4
-1 -1 0 1
5
-1 -1 -1 0 0
```

**Output

```text
3
1
4
```

## Complexity Analysis

- **Time Complexity:** `O(n)` per test case.
- **Space Complexity:** `O(1)` auxiliary space, excluding the input array.

## Key Takeaway

Make every zero positive first, then ensure the number of negative elements is even. If it is odd, converting one `-1` into `1` requires two additional operations.
