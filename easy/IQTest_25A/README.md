# IQ Test

## Problem

Given `n` integers, exactly one number differs from the others in parity (even/odd). Find the **1-based index** of that unique number.

### Example

**Input**

```
5
2 4 7 8 10
```

**Output**

```
3
```

## Approach

* Count the number of even and odd integers.
* Determine the majority parity.
* Traverse the array again and find the element with the opposite parity.
* Print its 1-based index.

## Algorithm

1. Read `n` and the list of numbers.
2. Count even and odd numbers.
3. Identify the majority parity.
4. Find the index of the unique number with different parity.
5. Output the index.

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)` (excluding the input list)

## Key Concepts

* Parity (Even/Odd)
* Counting
* Linear Traversal
