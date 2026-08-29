# A. Little Elephant and Rozdil

## Problem Statement

The Little Elephant wants to leave Rozdil and travel to another city. For each city, the travel time from Rozdil is given.

He will choose the city with the **minimum travel time**. However, if multiple cities have the same minimum travel time, he will stay in Rozdil.

The task is to determine the destination city or print `Still Rozdil`.

## Approach

1. Read the number of cities `n`.
2. Store the travel times in a list.
3. Find the minimum travel time.
4. Count how many times this minimum occurs:

   * If it occurs exactly once, print the corresponding city number.
   * Otherwise, print `Still Rozdil`.

Python uses **0-based indexing**, while cities are numbered from **1**, so we add `1` to the index.

## Python Solution

```python
n = int(input())
times = list(map(int, input().split()))

minimum = min(times)

if times.count(minimum) == 1:
    print(times.index(minimum) + 1)
else:
    print("Still Rozdil")
```

## Example

### Input

```text
7
7 4 47 100 4 9 12
```

### Output

```text
Still Rozdil
```

### Explanation

The minimum travel time is `4`, but it occurs for both city `2` and city `5`.

Since there are multiple cities with the minimum travel time, the answer is:

`Still Rozdil`

## Complexity

* **Time:** `O(n)`
* **Space:** `O(n)`

## Key Concept

**Find the minimum value and verify that it is unique.**
