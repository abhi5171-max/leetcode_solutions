# A. Life Without Zeros

## Problem

Given two positive integers `a` and `b`, calculate:

```text
c = a + b
```

Then remove all zero digits from `a`, `b`, and `c`.

The task is to determine whether the equation remains correct after removing all zeros.

## Approach

1. Read `a` and `b`.
2. Calculate `c = a + b`.
3. Remove all `0` digits from `a`, `b`, and `c`.
4. Check whether:

```text
removeZeros(a) + removeZeros(b) == removeZeros(c)
```

5. Print `YES` if the equation is correct; otherwise print `NO`.

## Example

### Input

```text
101
102
```

### Processing

```text
101 → 11
102 → 12
203 → 23

11 + 12 = 23
```

### Output

```text
YES
```

## Complexity

* **Time:** `O(log(a + b))`
* **Space:** `O(log(a + b))`

## Language

* Python 3

## Key Concept

* String manipulation
* Arithmetic operations
* Digit removal
