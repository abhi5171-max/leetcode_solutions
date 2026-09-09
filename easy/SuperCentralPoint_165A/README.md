# A. Supercentral Point

## Problem Description

You are given `n` distinct points on a Cartesian coordinate system.

A point `(x, y)` is called **supercentral** if there is at least:

* One point to its **left**
* One point to its **right**
* One point **above** it
* One point **below** it

The task is to count the total number of supercentral points.

## Conditions

For a point `(x, y)`:

* **Left neighbor:** `(x', y)` where `x' < x`
* **Right neighbor:** `(x', y)` where `x' > x`
* **Lower neighbor:** `(x, y')` where `y' < y`
* **Upper neighbor:** `(x, y')` where `y' > y`

A point is supercentral only when all four types of neighbors exist.

## Approach

For each point, check every other point and determine whether it has:

* A left neighbor
* A right neighbor
* An upper neighbor
* A lower neighbor

If all four conditions are satisfied, increase the answer by `1`.

Since `n ≤ 200`, using nested loops is efficient enough.

## Algorithm

1. Read `n` and store all points.
2. Initialize `answer = 0`.
3. For every point `(x, y)`:

   * Check all other points.
   * Find whether left, right, upper, and lower neighbors exist.
4. If all four neighbors exist, increment `answer`.
5. Print the final answer.

## Complexity

* **Time Complexity:** `O(n²)`
* **Space Complexity:** `O(n)`

## Python Solution

```python
n = int(input())

points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

answer = 0

for x, y in points:
    left = right = upper = lower = False

    for x2, y2 in points:
        if y2 == y and x2 < x:
            left = True
        if y2 == y and x2 > x:
            right = True
        if x2 == x and y2 < y:
            lower = True
        if x2 == x and y2 > y:
            upper = True

    if left and right and upper and lower:
        answer += 1

print(answer)
```

## Example

### Input

```text
5
0 0
0 1
1 0
0 -1
-1 0
```

### Output

```text
1
