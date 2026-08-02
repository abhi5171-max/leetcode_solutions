# A. Second Order Statistics

## Problem

Given a sequence of integers, determine the **second order statistic**, which is defined as the smallest element that is **strictly greater than the minimum**. If no such element exists, print `NO`.

## Approach

* Read the input sequence.
* Remove duplicate values using a `set`.
* Sort the unique elements.
* If there are fewer than two unique elements, output `NO`.
* Otherwise, output the second smallest unique element.

## Algorithm

1. Read `n` and the array.
2. Convert the array to a set to eliminate duplicates.
3. Sort the unique values.
4. Check the number of unique elements:

   * If less than 2, print `NO`.
   * Otherwise, print the second element in the sorted list.

## Complexity

* **Time Complexity:** `O(n log n)`
* **Space Complexity:** `O(n)`

## Python Solution

```python
n = int(input())
arr = list(map(int, input().split()))

unique = sorted(set(arr))

if len(unique) < 2:
    print("NO")
else:
    print(unique[1])
```

## Example

**Input**

```
5
1 2 3 1 1
```

**Output**

```
2
```

## Key Concepts

* Sets
* Sorting
* Arrays
* Basic Implementation
