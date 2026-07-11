# Sequence Replacement

## Problem

Given a sequence containing only the numbers **1**, **2**, and **3**, determine the minimum number of replacements required to make every element in the sequence equal.

## Example

**Input**

```text
9
1 3 2 2 2 1 1 2 3
```

**Output**

```text
5
```

## Approach

* Count the frequency of each number (`1`, `2`, and `3`).
* Keep the number that appears the most.
* Replace every other number with the most frequent one.
* The minimum replacements equal:

  * `n - (maximum frequency)`

## Algorithm

1. Read the input sequence.
2. Count the occurrences of `1`, `2`, and `3`.
3. Find the maximum frequency.
4. Print `n - maximum_frequency`.

## Complexity

* **Time Complexity:** `O(n)`
* **Space Complexity:** `O(1)`

## Key Concepts

* Frequency Counting
* Greedy Strategy
* Arrays
* Linear Traversal
